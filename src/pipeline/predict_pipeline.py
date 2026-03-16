import sys
import os

from src.exception import CustomException
from src.logger import logging
from src.utils import load_object
import pandas as pd

class Predict:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

            preprocessor = load_object(os.path.join(BASE_DIR, 'artifacts', 'preprocessor.pkl'))
            model = load_object(os.path.join(BASE_DIR, 'artifacts', 'model.pkl'))

            data_scaled = preprocessor.transform(features)
            result = model.predict(data_scaled)

            return result
        except Exception as e:
            logging.exception('Error occurred at predict pipeline')
            raise CustomException(e, sys)
        
class CustomData:
    def __init__(self, MSSubClass: int,	MSZoning: str, LotFrontage: float, LotArea: int, LotShape: str,	LandContour: str, LotConfig: str, LandSlope: str, Neighborhood: float, Condition1: str,	BldgType: str,	HouseStyle: str, OverallQual: int,	OverallCond: int, YearBuilt: int, YearRemodAdd: int, RoofStyle: str,Exterior1st: int, MasVnrArea: float, ExterQual: str, ExterCond: str, Foundation: str, BsmtQual: str,BsmtCond: str, BsmtExposure: str, BsmtFinType1: str, BsmtFinSF1: int, BsmtFinType2: str, BsmtFinSF2: int,BsmtUnfSF: int, TotalBsmtSF: int, Heating: str, HeatingQC: str, CentralAir: str, Electrical: str,_1stFlrSF: int, _2ndFlrSF: int, LowQualFinSF: int, GrLivArea: int, BsmtFullBath: int, BsmtHalfBath: int,FullBath: int, HalfBath: int, BedroomAbvGr: int, KitchenAbvGr: int, KitchenQual: str, TotRmsAbvGrd: int,Functional: str, Fireplaces: int, FireplaceQu: str, GarageType: str, GarageYrBlt: float, GarageFinish: str, GarageCars: int, GarageArea: int, GarageQual: str, GarageCond: str, PavedDrive: str, WoodDeckSF: int, OpenPorchSF: int, EnclosedPorch: int, _3SsnPorch: int, ScreenPorch: int, PoolArea: int, MiscVal: int,	MoSold: int, YrSold: int, SaleType: float, SaleCondition: str):
        self.MSSubClass = MSSubClass
        self.MSZoning = MSZoning
        self.LotFrontage = LotFrontage
        self.LotArea = LotArea
        self.LotShape = LotShape
        self.LandContour = LandContour
        self.LotConfig = LotConfig
        self.LandSlope = LandSlope
        self.Neighborhood = Neighborhood
        self.Condition1 = Condition1
        self.BldgType = BldgType
        self.HouseStyle = HouseStyle
        self.OverallQual = OverallQual
        self.OverallCond = OverallCond
        self.YearBuilt = YearBuilt
        self.YearRemodAdd = YearRemodAdd
        self.RoofStyle = RoofStyle
        self.Exterior1st = Exterior1st
        self.MasVnrArea = MasVnrArea
        self.ExterQual = ExterQual
        self.ExterCond = ExterCond
        self.Foundation = Foundation
        self.BsmtQual = BsmtQual
        self.BsmtCond = BsmtCond
        self.BsmtExposure = BsmtExposure
        self.BsmtFinType1 = BsmtFinType1
        self.BsmtFinSF1 = BsmtFinSF1
        self.BsmtFinType2 = BsmtFinType2
        self.BsmtFinSF2 = BsmtFinSF2
        self.BsmtUnfSF = BsmtUnfSF
        self.TotalBsmtSF = TotalBsmtSF
        self.Heating = Heating
        self.HeatingQC = HeatingQC
        self.CentralAir = CentralAir
        self.Electrical = Electrical
        self._1stFlrSF = _1stFlrSF
        self._2ndFlrSF = _2ndFlrSF
        self.LowQualFinSF = LowQualFinSF
        self.GrLivArea = GrLivArea
        self.BsmtFullBath = BsmtFullBath
        self.BsmtHalfBath = BsmtHalfBath
        self.FullBath = FullBath
        self.HalfBath = HalfBath
        self.BedroomAbvGr = BedroomAbvGr
        self.KitchenAbvGr = KitchenAbvGr
        self.KitchenQual = KitchenQual
        self.TotRmsAbvGrd = TotRmsAbvGrd
        self.Functional = Functional
        self.Fireplaces = Fireplaces
        self.FireplaceQu = FireplaceQu
        self.GarageType = GarageType
        self.GarageYrBlt = GarageYrBlt
        self.GarageFinish = GarageFinish
        self.GarageCars = GarageCars
        self.GarageArea = GarageArea
        self.GarageQual = GarageQual
        self.GarageCond = GarageCond
        self.PavedDrive = PavedDrive
        self.WoodDeckSF = WoodDeckSF
        self.OpenPorchSF = OpenPorchSF
        self.EnclosedPorch = EnclosedPorch
        self._3SsnPorch = _3SsnPorch
        self.ScreenPorch = ScreenPorch
        self.PoolArea = PoolArea
        self.MiscVal = MiscVal
        self.MoSold = MoSold
        self.YrSold = YrSold
        self.SaleType = SaleType
        self.SaleCondition = SaleCondition
 
    def get_data_as_dataframe(self):
        try:
            data = {
                'MSSubClass': [self.MSSubClass],
                'MSZoning': [self.MSZoning],
                'LotFrontage': [self.LotFrontage],
                'LotArea': [self.LotArea],
                'LotShape': [self.LotShape],
                'LandContour': [self.LandContour],
                'LotConfig': [self.LotConfig],
                'LandSlope': [self.LandSlope],
                'Neighborhood': [self.Neighborhood],
                'Condition1': [self.Condition1],
                'BldgType': [self.BldgType],
                'HouseStyle': [self.HouseStyle],
                'OverallQual': [self.OverallQual],
                'OverallCond': [self.OverallCond],
                'YearBuilt': [self.YearBuilt],
                'YearRemodAdd': [self.YearRemodAdd],
                'RoofStyle': [self.RoofStyle],
                'Exterior1st': [self.Exterior1st],
                'MasVnrArea': [self.MasVnrArea],
                'ExterQual': [self.ExterQual],
                'ExterCond': [self.ExterCond],
                'Foundation': [self.Foundation],
                'BsmtQual': [self.BsmtQual],
                'BsmtCond': [self.BsmtCond],
                'BsmtExposure': [self.BsmtExposure],
                'BsmtFinType1': [self.BsmtFinType1],
                'BsmtFinSF1': [self.BsmtFinSF1],
                'BsmtFinType2': [self.BsmtFinType2],
                'BsmtFinSF2': [self.BsmtFinSF2],
                'BsmtUnfSF': [self.BsmtUnfSF],
                'TotalBsmtSF': [self.TotalBsmtSF],
                'Heating': [self.Heating],
                'HeatingQC': [self.HeatingQC],
                'CentralAir': [self.CentralAir],
                'Electrical': [self.Electrical],
                '1stFlrSF': [self._1stFlrSF],
                '2ndFlrSF': [self._2ndFlrSF],
                'LowQualFinSF': [self.LowQualFinSF],
                'GrLivArea': [self.GrLivArea],
                'BsmtFullBath': [self.BsmtFullBath],
                'BsmtHalfBath': [self.BsmtHalfBath],
                'FullBath': [self.FullBath],
                'HalfBath': [self.HalfBath],
                'BedroomAbvGr': [self.BedroomAbvGr],
                'KitchenAbvGr': [self.KitchenAbvGr],
                'KitchenQual': [self.KitchenQual],
                'TotRmsAbvGrd': [self.TotRmsAbvGrd],
                'Functional': [self.Functional],
                'Fireplaces': [self.Fireplaces],
                'FireplaceQu': [self.FireplaceQu],
                'GarageType': [self.GarageType],
                'GarageYrBlt': [self.GarageYrBlt],
                'GarageFinish': [self.GarageFinish],
                'GarageCars': [self.GarageCars],
                'GarageArea': [self.GarageArea],
                'GarageQual': [self.GarageQual],
                'GarageCond': [self.GarageCond],
                'PavedDrive': [self.PavedDrive],
                'WoodDeckSF': [self.WoodDeckSF],
                'OpenPorchSF': [self.OpenPorchSF],
                'EnclosedPorch': [self.EnclosedPorch],
                '3SsnPorch': [self._3SsnPorch],
                'ScreenPorch': [self.ScreenPorch],
                'PoolArea': [self.PoolArea],
                'MiscVal': [self.MiscVal],
                'MoSold': [self.MoSold],
                'YrSold': [self.YrSold],
                'SaleType': [self.SaleType],
                'SaleCondition': [self.SaleCondition],
            }
            return pd.DataFrame(data)
        except Exception as e:
            logging.exception('Error occurred at predict pipeline')
            raise CustomException(e, sys)