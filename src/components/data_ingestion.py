import os
import sys
from src.logger import logging
from src.exception import CustomException
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    raw_data_path :str = os.path.join('artifacts', 'raw.csv')
    train_data_path :str = os.path.join('artifacts', 'train.csv')
    test_data_path :str = os.path.join('artifacts', 'test.csv')

class DataIngestion:
    def __init__(self):
        self.data_ingestion_obj = DataIngestionConfig()

    def start_data_ingestion(self):
        logging.info('Data Ingestion Strated')
        try:
            data_path = os.path.join(os.getcwd(), 'data', 'train.csv')
            df = pd.read_csv(data_path)
            logging.info('Data read as pandas dataframe')

            os.makedirs(os.path.dirname(self.data_ingestion_obj.raw_data_path), exist_ok = True)
            df.to_csv(self.data_ingestion_obj.raw_data_path, index = False, header = True)

            train_data, test_data = train_test_split(df, random_state = 42, test_size = 0.2)
            train_data.to_csv(self.data_ingestion_obj.train_data_path, index = False, header = True)
            test_data.to_csv(self.data_ingestion_obj.test_data_path, index = False, header = True)

            logging.info('Ingestion complete')
            return(
                self.data_ingestion_obj.train_data_path,
                self.data_ingestion_obj.test_data_path
            )

        except Exception as e:
            logging.exception('Exception occurred in data ingestion')
            raise CustomException(e, sys)
        
if __name__ == '__main__':
    obj = DataIngestion()
    train_path, test_path = obj.start_data_ingestion()

    data_transformation_obj = DataTransformation()
    train_arr, test_arr, _ = data_transformation_obj.initiate_data_transformation(train_path, test_path)

    model_trainer = ModelTrainer()
    model_trainer.initiate_training(train_arr, test_arr)