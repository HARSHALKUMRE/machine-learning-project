from housing.pipeline.training_pipeline import TrainingPipeline
from housing.exception import HousingException
from housing.logger import logging

def main():
    try:
        training_pipeline = TrainingPipeline()
        training_pipeline.run_pipeline()
    except Exception as e:
        logging.error(f"{e}")
        print(e)
        
    
if __name__=="__main__":
    main()