import numpy as np
import pandas as pd
import os
import sys
from dataclasses import dataclass

from sklearn.preprocessing import OrdinalEncoder, StandardScaler, OneHotEncoder
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.linear_model import Ridge, Lasso, LinearRegression
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor
from catboost import CatBoostRegressor

from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

from src.exception import CustomException
from src.logger import logging
from src.utils import save_obj, evaluate_model

@dataclass
class ModelTrainerConfig:
    model_path: str = os.path.join('artifacts', 'model.pkl')

class ModelTrainer:
    def __init__(self):
        self.model_path_config = ModelTrainerConfig()

    def initiate_training(self, train, test):
        try:
            logging.info('Training started')

            logging.info('Splitting data')

            X_train, y_train, X_test, y_test = (
                train[:, :-1],
                train[:, -1],
                test[:, :-1],
                test[:, -1]
            )

            models = {
                'LinearRegression': LinearRegression(),
                'Ridge': Ridge(),
                'Lasso': Lasso(),
                'RandomForestRegressor': RandomForestRegressor(),
                'AdaBoostRegressor': AdaBoostRegressor(),
                'DecisionTreeRegressor': DecisionTreeRegressor(),
                'XGBRegressor': XGBRegressor(),
                'CatBoostRegressor': CatBoostRegressor(verbose = False)
            }

            report: dict = evaluate_model(models, X_train, X_test, y_train, y_test)
            print('=' * 50)
            print(f'Model report: {report}')
            logging.info('Model report: ', report)

            best_score = max(sorted(report.values()))

            best_model_name = list(report.keys())[
                list(report.values()).index(best_score)
            ]

            if best_score < 0.6:
                logging.info('Low model score < 0.6')
                raise CustomException('No best model found')
            
            print(f'Best model: {best_model_name}, w/score: {best_score}')
            logging.info(f'Best model: {best_model_name}, w/score: {best_score}')

            save_obj(
                self.model_path_config.model_path,
                obj = models[best_model_name]
            )
            logging.info('Model saved')
        except Exception as e:
            logging.exception('Error occurred at model training')
            raise CustomException(e, sys)