import os
import docker
import docker.errors
import logging
from fastapi import HTTPException
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from .models.upper_models import ConfigurationFile
import pytomlpp


logging.basicConfig(level=logging.INFO)


DOTENV = os.path.join(os.path.dirname(__file__), ".env")

class Settings(BaseSettings):
    CONFIGURATION_FILE_PATH: str = Field(..., env="CONFIGURATION_FILE_PATH")
    CONFIGURATION_FILE_NAME: str = Field(..., env="CONFIGURATION_FILE_NAME")
    TELEGRAF_IMAGE: str = Field(..., env="TELEGRAF_IMAGE")

    model_config = SettingsConfigDict(env_file=DOTENV, env_file_encoding='utf-8')


variables = Settings()

docker_client = docker.from_env()


def deserialize(data_or_filepath: str, file: bool = False) -> ConfigurationFile:
    """
    Deserialize TOML content or file into ConfigurationFile object.
    :param data_or_filepath: Content or path to TOML file.
    :param file: Whether the input is a file.
    :return: Pydantic ConfigurationFile object.
    """
    try:
        if file:
            with open(data_or_filepath, encoding="utf-8") as file:
                toml_file = pytomlpp.load(file)
                validated_content = ConfigurationFile(**toml_file)
                logging.info(f"Success! File loaded: {data_or_filepath}")
                return validated_content
        else:
            toml_data = pytomlpp.loads(data_or_filepath)
            return ConfigurationFile(**toml_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Server error: {str(e)}")


def serialize(data: ConfigurationFile, save_to_file: bool = False, filename: str = "./container_name.conf") -> str | None:
    """
    Serialize a Pydantic model into a TOML string or file.
    
    :param data: Pydantic model to serialize.
    :param save_to_file: Whether to save the output to a file.
    :param filename: Path to the file for saving (if applicable).
    :return: Serialized TOML string if save_to_file=False, otherwise None.
    """
    try:
        serialized_data = data.model_dump(exclude_unset=True)

        if save_to_file:
            os.makedirs(os.path.dirname(filename), exist_ok=True)

            with open(filename, mode="w", encoding="utf-8") as file_obj:
                pytomlpp.dump(serialized_data, file_obj)
                logging.info(f"Configuration serialized and saved to {filename}")
            return None
        else:
            return pytomlpp.dumps(serialized_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error serializing configuration: {str(e)}")


def serialize(data: ConfigurationFile, save_to_file: bool = False, filename: str = "./container_name.conf") -> str | None:
    """
    Serialize a Pydantic model into a TOML string or file.
    
    :param data: Pydantic model to serialize.
    :param save_to_file: Whether to save the output to a file.
    :param filename: Path to the file for saving (if applicable).
    :return: Serialized TOML string if save_to_file=False, otherwise None.
    """
    try:
        serialized_data = data.model_dump(exclude_unset=True)

        if save_to_file:
            os.makedirs(os.path.dirname(filename), exist_ok=True)

            with open(filename, mode="w", encoding="utf-8") as file_obj:
                pytomlpp.dump(serialized_data, file_obj)
                logging.info(f"Configuration serialized and saved to {filename}")
            return None
        else:
            return pytomlpp.dumps(serialized_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error serializing configuration: {str(e)}")


# def parser(filepath: str, filepath2: str):
#     with open(filepath, 'r') as source, open(filepath2, 'a') as destination:
#         for name in source:
#             class_name = name.strip()
#             if class_name:
#                 destination.write(f"class {class_name}(CommonAggregatorsParams):\n    pass\n\n")

# parser(r"D:\Work\app\models\parser.txt", r"D:\Work\app\models\aggregators.py")

# def correct_toml(filepath: str) -> None:
#     try:
#         ready_toml = []
#         skip_line = ("[", )
#         with open(filepath, mode="r+", encoding="utf-8") as file:
#             for line in file.readlines():
#                 if not line.startswith(skip_line):
#                     updated_line = "  " + line
#                     ready_toml.append(updated_line)

#         return "\n".join(ready_toml)

#     except FileNotFoundError:
#         raise HTTPException(status_code=500, detail="Server error. Toml file not found")
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Server error. {e}")
    

# result = correct_toml(r"D:\Work\app\active_containers\cpu2.conf")