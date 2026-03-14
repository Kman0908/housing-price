import os
import sys
from dataclasses import dataclass
import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder, StandardScaler, TargetEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from src.logger import logging
from src.exception import CustomException
from src.utils import save_obj

@dataclass
class DataTransfromationConfig:
    preprocessor_obj_path :str = os.path.join('artifacts', 'preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransfromationConfig()

    def get_data_transformation_obj(self):
        try:
            num_cols = ['MSSubClass', 'LotFrontage', 'LotArea', 'OverallQual', 'OverallCond', 'YearBuilt', 'YearRemodAdd', 'MasVnrArea','BsmtFinSF1', 'BsmtFinSF2', 'BsmtUnfSF', 'TotalBsmtSF', '1stFlrSF', '2ndFlrSF', 'LowQualFinSF', 'GrLivArea', 'BsmtFullBath', 'BsmtHalfBath', 'FullBath', 'HalfBath', 'BedroomAbvGr', 'KitchenAbvGr', 'TotRmsAbvGrd', 'Fireplaces', 'GarageYrBlt', 'GarageCars', 'GarageArea', 'WoodDeckSF', 'OpenPorchSF', 'EnclosedPorch', '3SsnPorch', 'ScreenPorch', 'PoolArea', 'MiscVal', 'MoSold', 'YrSold']

            nominal_cols = ['MSZoning', 'LandContour', 'LotConfig', 'Condition1', 'BldgType', 'HouseStyle', 'RoofStyle', 'Foundation', 'Heating', 'CentralAir', 'GarageType', 'SaleCondition']

            ordinal_cols = ['LotShape', 'LandSlope', 'ExterQual', 'ExterCond', 'BsmtQual', 'BsmtCond', 'BsmtExposure', 'BsmtFinType1', 'BsmtFinType2', 'HeatingQC', 'Electrical', 'KitchenQual', 'Functional', 'FireplaceQu', 'GarageFinish', 'GarageQual', 'GarageCond', 'PavedDrive']

            # ordinal categories
            lShape = ['IR3', 'IR2', 'IR1', 'Reg']
            lSlope = ['Sev', 'Mod', 'Gtl']
            QualOrder = ['None', 'Po', 'Fa', 'TA', 'Gd', 'Ex']
            bsmt_quality_order = ['None', 'No', 'Mn', 'Av', 'Gd']
            bsmt_fin_order = ['None', 'Unf', 'LwQ', 'Rec', 'BLQ', 'ALQ', 'GLQ']
            Electrical_order = ['Mix', 'FuseP', 'FuseF', 'FuseA', 'SBrkr']
            Functional_order = ['Sal', 'Sev', 'Maj2', 'Maj1', 'Mod', 'Min2', 'Min1', 'Typ']
            Garage_Qual = ['None', 'Unf', 'RFn', 'Fin']
            Paved_drive = ['N', 'P', 'Y']

            target_cols = ['Neighborhood', 'Exterior1st', 'SaleType']

            num_pipeline = Pipeline(steps = [
                ('Impute', SimpleImputer(strategy = 'median')),
                ('Scalar', StandardScaler())
            ])

            ordinal_pipeline = Pipeline(steps = [
                ('Impute', SimpleImputer(strategy = 'constant', fill_value = 'None')),
                ('Encoder', OrdinalEncoder(categories = [
                    lShape, #LotShape
                    lSlope, #LotSlope
                    QualOrder, #ExterQual
                    QualOrder, #ExrterCond
                    QualOrder, #BsmtQual
                    QualOrder, #BsmtCond
                    bsmt_quality_order, #BasementExposure
                    bsmt_fin_order, #BsmtFinType1
                    bsmt_fin_order, #BsmtFinType2
                    QualOrder, #HeatingQc
                    Electrical_order, #Electrical
                    QualOrder, #KitchenQual
                    Functional_order, #Functional
                    QualOrder, #FireplaceQu
                    Garage_Qual, #GarageFinish
                    QualOrder, #GarageQual
                    QualOrder, #GarageCond
                    Paved_drive #PavedDrive
                ],
                handle_unknown = 'use_encoded_value',
                unknown_value = -1
                ))
            ])

            nominal_pipeline = Pipeline(steps = [
                ('Impute', SimpleImputer(strategy = 'constant', fill_value = 'None')),
                ('Encoder', OneHotEncoder(handle_unknown = 'ignore', sparse_output = False))
            ])

            target_pipeline = Pipeline(steps = [
                ('Impute', SimpleImputer(strategy = 'most_frequent')),
                ('Encoder', TargetEncoder(target_type = 'continuous'))
            ])

            preprocessor = ColumnTransformer(transformers = [
                ('num_pipeline', num_pipeline, num_cols),
                ('ordinal_pipeline', ordinal_pipeline, ordinal_cols),
                ('nominal_pipeline', nominal_pipeline, nominal_cols),
                ('target_pipeline', target_pipeline, target_cols),
            ])

            return preprocessor
        
        except Exception as e:
            logging.exception('Exception occurred at data transformation')
            raise CustomException(e, sys)
        
    def initiate_data_transformation(self, train_path, test_path):
        try:
            logging.info('Data transformation started')

            train_data = pd.read_csv(train_path)
            test_data = pd.read_csv(test_path)

            logging.info('Data read as pandas dataframe')
            logging.info(f'Train data sample: {train_data.head()}')
            logging.info(f'Test data sample: {test_data.head()}')

            logging.info('Got preprocessor')
            preprocessor = self.get_data_transformation_obj()

            target_col = 'SalePrice'
            drop_cols = ['Alley', 'MasVnrType', 'PoolQC', 'Fence', 'MiscFeature', 'Id', 'SalePrice']

            input_train = train_data.drop(columns = drop_cols)
            input_test = test_data.drop(columns = drop_cols)

            target_train = train_data[target_col]
            target_test = test_data[target_col]

            train_data['Heating'] = train_data['Heating'].apply(
                lambda x: x if x == 'GasA' else 'Other'
            )
            test_data['Heating'] = test_data['Heating'].apply(
                lambda x: x if x == 'GasA' else 'Other'
            )

            logging.info('Preprocessing Started')
            input_train = preprocessor.fit_transform(input_train, target_train)
            input_test = preprocessor.transform(input_test)

            train_arr = np.c_[input_train, np.array(target_train)]
            test_arr = np.c_[input_test, np.array(target_test)]

            save_obj(
                self.data_transformation_config.preprocessor_obj_path,
                preprocessor
            )
            logging.info('Preprocessor saved')

            return train_arr, test_arr, self.data_transformation_config.preprocessor_obj_path

        except Exception as e:
            logging.exception('Exception occurred at data transformation')
            raise CustomException(e, sys)