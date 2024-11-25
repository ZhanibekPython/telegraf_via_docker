import os
import docker
import docker.errors
import logging
from fastapi import HTTPException
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from .models.upper_models import ConfigurationFile
from tomlkit import document, table, array, dumps
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

def generate_telegraf_toml_with_nested_support(json_data: dict) -> str:
    """
    Генерирует TOML для Telegraf с поддержкой вложенных структур.

    :param json_data: Словарь с конфигурацией.
    :return: Сериализованный TOML как строка.
    """
    def process_value(value):
        """Recursively processes data"""
        if isinstance(value, dict):
            tbl = table(True)
            for k, v in value.items():
                inner_table = table()
                inner_table.add(k, process_value(v))
                tbl.add(k, inner_table)
            return tbl
        elif isinstance(value, list):
            arr = array()
            for item in value:
                arr.append(process_value(item))
            return arr
        else:
            return value

    doc = document()

    if "global_tags" in json_data:
        result = json_data["global_tags"]
        doc.add("global_tags", result)

    if "secretstores" in json_data:
        result = json_data["secretstores"]
        doc.add("secretstores", result)

    if "agent" in json_data:
        result = json_data["agent"]
        doc.add("agent", result)
        
    if "inputs" in json_data:
        result = json_data["inputs"]
        doc.add("inputs", result)

    if "processors" in json_data:
        result = json_data["processors"]
        doc.add("processors", result)

    if "aggregators" in json_data:
        result = json_data["aggregators"]
        doc.add("aggregators", result)

    if "outputs" in json_data:
        result = json_data["outputs"]
        doc.add("outputs", result)


    raw_toml = dumps(doc)

    formatted_toml = []
    for line in raw_toml.splitlines():
        if line.startswith("[") or not line.strip():
            formatted_toml.append(line)
        else:
            formatted_toml.append(f"  {line}")

    return "\n".join(formatted_toml)

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


# def parser(filepath: str, filepath2: str):
#     with open(filepath, 'r') as source, open(filepath2, 'a') as destination:
#         for name in source:
#             class_name = name.strip()
#             if class_name:
#                 destination.write(f"class {class_name}(CommonAggregatorsParams):\n    pass\n\n")

# parser(r"D:\Work\app\models\parser.txt", r"D:\Work\app\models\aggregators.py")



# with open(filepath, "r", encoding="utf-8") as file:
#     json_data = json.load(file)

# result = generate_telegraf_toml_with_nested_support(json_data)
# print(result)