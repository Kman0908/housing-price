import os
import sys
import pickle
from src.exception import CustomException
from src.logger import logging
from sklearn.metrics import r2_score

def save_obj(path, obj):
    try:
        dir_path = os.path.dirname(path)
        os.makedirs(dir_path, exist_ok = True)
        
        with open(path, 'wb') as f:
            pickle.dump(obj, f)
    except Exception as e:
        logging.exception('Exception occurred at utils.save_obj')
        raise CustomException(e, sys)
    
def evaluate_model(models: dict, X_train, X_test, y_train, y_test):
    try:
        report = {}

        for i in range(len(models)):
            model = list(models.values())[i]

            model.fit(X_train, y_train)
            y_pred_train = model.predict(X_train)
            y_pred_test = model.predict(X_test)

            train_score = r2_score(y_train, y_pred_train)
            test_score = r2_score(y_test, y_pred_test)

            report[list(models.keys())[i]] = test_score

        return report
    except Exception as e:
        logging.exception('Exception occurred at utils.evaluate_model')
        raise CustomException(e, sys)
    
def load_object(path: str):
    try:
        with open(path, 'rb') as f:
            return pickle.load(f)
    except Exception as e:
        logging.exception('Error occurred at at utils.load_object')
        raise CustomException(e, sys)