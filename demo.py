from housing.pipeline.training_pipeline import TrainingPipeline
from housing.exception import HousingException
from housing.logger import logging
from housing.config.configuration import Configuration
from housing.component.data_transformation import DataTransformation
import os

def main():
    try:
        config_path = os.path.join("config", "config.yaml")
        training_pipeline = TrainingPipeline(Configuration(config_file_path=config_path))
        #training_pipeline.run_pipeline()
        training_pipeline.start()
        logging.info("main function execution completed.")
        #data_validation_config = Configuration().get_data_validation_config()
        #print(data_validation_config)
        
        #data_transformation_config = Configuration().get_data_transformation_config()
        #print(data_transformation_config)
        #schema_file_path = r"G:\100-days-of-dl\Krish Naik\FSDS Ineuron Course\projects\machine-learning-project\config\schema.yaml"
        #file_path = r"G:\100-days-of-dl\Krish Naik\FSDS Ineuron Course\projects\machine-learning-project\housing\artifact\data_ingestion\2023-02-01-11-42-50\ingested_data\train\housing.csv"
        #df = DataTransformation.load_data(file_path=file_path, schema_file_path=schema_file_path)
        #print(df.columns)
        #print(df.dtypes)
        
        #model_evaluation_config = Configuration().get_model_evaluation_config()
        #print(model_evaluation_config)
        
    except Exception as e:
        logging.error(f"{e}")
        print(e)
        
    
if __name__=="__main__":
    main()