import os
import sys
import pickle
from src.exception import CustomException
from src.logger import logging

def save_obj(path, obj):
    try:
        dir_path = os.path.dirname(path)
        os.makedirs(dir_path, exist_ok = True)
        
        with open(path, 'wb') as f:
            pickle.dump(obj, f)
    except Exception as e:
        logging.exception('Exception occurred at utils.save_obj')
        raise CustomException(e, sys)