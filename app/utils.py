import toml
import logging
from fastapi import HTTPException
import os
import docker
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


logging.basicConfig(level=logging.INFO)

DOTENV = os.path.join(os.path.dirname(__file__), ".env")


class Settings(BaseSettings):
    CONFIGURATION_FILE_PATH: str = Field(..., env="CONFIGURATION_FILE_PATH")
    
    model_config = SettingsConfigDict(env_file=DOTENV, env_file_encoding='utf-8')

variables = Settings()

def check_file_exists(filepath: str) -> bool:
    """This function checks if file exists"""
    if not os.path.exists(filepath):
        logging.error(f"File not found: {filepath}")
        raise HTTPException(status_code=500, detail="Server error. File was not found")
    return True


def deserialize(filepath: str) -> dict:
    """This function converts toml to dict"""
    check_file_exists(filepath)

    try:
        with open(filepath, encoding="utf-8") as file:
            toml_file = toml.load(file)
        logging.info(f"Success! File loaded: {filepath}")
        return toml_file
    except (FileNotFoundError, toml.TomlDecodeError) as e:
        logging.error(f"Error while opening the file: {e}")
        raise HTTPException(status_code=500, detail="Server error. Configuration file damaged")


def serialize(filepath: str, data: dict) -> str:
    """This function converts dict to toml"""
    check_file_exists(filepath)

    if not isinstance(data, dict):
        logging.error("The data must be dict-typed")
        raise HTTPException(status_code=400, detail="Input data is not a dictionary")

    try:
        with open(filepath, "w", encoding="utf-8") as file:
            toml.dump(data, file)
        logging.info(f"Success! File was updated: {filepath}")
        return "Updated configuration file was saved successfully"
    except (FileNotFoundError, toml.TomlDecodeError, OSError) as e:
        logging.error(f"Error while dumping the file: {e}")
        raise HTTPException(status_code=500, detail="Server error. Failed to update configuration file")

def parser(filepath: str, filepath2: str):
    with open(filepath, 'r') as source, open(filepath2, 'a') as destination:
        for name in source:
            class_name = name.strip()
            if class_name:
                destination.write(f"class {class_name}(CommonAggregatorsParams):\n    pass\n\n")

# parser(r"D:\Work\app\models\parser.txt", r"D:\Work\app\models\aggregators.py")


def create_docker_container(new_container_name: str, config_file_path: str = "/etc/telegraf/telegraf.conf", docker_image_name: str = "telegraf:1.31", volume_conf_file_path: str = "/etc/telegraf/telegraf.conf"):
    """This function creates a new docker container with given image_name and one volume presetting"""

    try:
        docker_client = docker.from_env()

        container = docker_client.containers.run(
            image=docker_image_name,
            detach=True,
            volumes={
                config_file_path: {"bind": volume_conf_file_path, "mode": "rw"}
            },
            name=new_container_name
        )
        return container.id
    except docker.errors.ContainerError as e:
        raise HTTPException(status_code=500, detail=f"Docker error: {str(e)}")
    