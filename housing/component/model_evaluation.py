from housing.exception import HousingException
from housing.logger import logging
import os,sys
from housing.entity.config_entity import ModelEvaluationConfig
from housing.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact, DataTransformationArtifact, ModelTrainerArtifact
from housing.utils.main_utils import write_yaml_file, read_yaml_file, load_object, load_data
from housing.constant import *
import numpy as np

class ModelEvaluation:
    
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise HousingException(e,sys) from e