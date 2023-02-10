from flask import Flask, request
import sys

import pip
from housing.utils.main_utils import read_yaml_file, write_yaml_file
from matplotlib.style import context
from housing.logger import logging
from housing.exception import HousingException
import os,sys
import json
from housing.config.configuration import Configuration
from housing.constant import CONFIG_DIR, get_current_time_stamp
from housing.pipeline.training_pipeline import TrainingPipeline
from housing.entity.housing_predictor import HousingPredictor, HousingData
from flask import send_file, abort, render_template

ROOT_DIR = os.getcwd()
LOG_FOLDER_NAME = "housing_log"
PIPELINE_FOLDER_NAME = "housing"
SAVED_MODELS_DIR_NAME = "saved_models"
MODEL_CONFIG_FILE_PATH = os.path.join(ROOT_DIR, CONFIG_DIR, "model.yaml")
LOG_DIR = os.path.join(ROOT_DIR, LOG_FOLDER_NAME)
PIPELINE_DIR = os.path.join(ROOT_DIR, PIPELINE_FOLDER_NAME)
SAVED_MODELS_DIR = os.path.join(ROOT_DIR, SAVED_MODELS_DIR_NAME)

from housing.logger import get_log_dataframe

HOUSING_DATA_KAY = "housing_data"
MEDIAN_HOUSING_VALUE_KEY = "median_housing_value"

app = Flask(__name__)

@app.route("/artifact", defaults={"req_path": "housing"})
@app.route("/artifact/<path:req_path>")
def render_artifact_dir(req_path):
    os.makedirs("housing", exist_ok=True)
    # Joining the base and the requested path
    print(f"req_path: {req_path}")
    abs_path = os.path.join(req_path)
    print(abs_path)
    # Return 404 if path doesn't exist
    if not os.path.exists(abs_path):
        return abort(404)

    # check if path is a file and serve
    if os.path.isfile(abs_path):
        if ".html" in abs_path:
            with open(abs_path, "r", encoding="utf-8") as file:
                content = ""
                for line in file.readlines():
                    content = f"{content}{line}"
                return content
        return send_file(abs_path)
    
    # Show directory contents
    files = {os.path.join(abs_path, file_name): file_name for file_name in os.listdir(abs_path) if
             "artifact" is os.path.join(abs_path, file_name)}


    result = {
        "files": files,
        "parent_folder": os.path.dirname(abs_path),
        "parent_label": abs_path
    }
    return render_template("files.html", result=result)

@app.route("/", methods=["GET", "POST"])
def index():
    try:
        return render_template("index.html")
    except Exception as e:
        return str(e)



if __name__=="__main__":
    app.run(debug=True)