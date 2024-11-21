import os
import docker
import docker.errors
import toml
import logging
import tarfile
from fastapi import HTTPException
from pydantic import Field, BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict
from io import BytesIO
from .models.upper_models import ConfigurationFile


logging.basicConfig(level=logging.INFO)
docker_client = docker.from_env()

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
    

def get_containers():
    """This function returns a dict of all and active containers with statuses"""

    try:
        docker_client = docker.from_env()

        all_containers = {}
        running = []
        exited = []
        paused = []
        restarting = []

        for container in docker_client.containers.list(all=True):
            all_containers[container.name] = container.status
            if container.status == "running":
                running.append(container.name)
            elif container.status == "exited":
                exited.append(container.name)
            elif container.status == "paused":
                paused.append(container.name)
            elif container.status == "restarting":
                restarting.append(container.name)
        
        return {"containers": all_containers,
                "running": running,
                "exited": exited,
                "paused": paused,
                "restarting": restarting}

    except docker.errors.ContainerError as e:
        raise HTTPException(status_code=500, detail=f"Docker error: {str(e)}")


def get_container_config(container_name: str, file_path: str = "/etc/telegraf/telegraf.conf"):
    """This function retrieves the config file from a running container."""

    try:
        container = docker_client.containers.get(container_name)

        tarstream, _ = container.get_archive(file_path)

        file_content = b''.join(tarstream)
        tar = tarfile.open(fileobj=BytesIO(file_content))

        file_name = file_path.lstrip("/")
        extracted_file = tar.extractfile(file_name)

        if extracted_file is None:
            raise HTTPException(status_code=404, detail="File not found in the container")

        content = extracted_file.read().decode("utf-8")

        deserialized_content = deserialize(content)

        validated_content = ConfigurationFile(**deserialized_content)
        
        save_path = f"./{container_name}.conf"
        with open(save_path, "w", encoding="utf-8") as file:
            file.write(content)

        return validated_content.model_dump(exclude_unset=True)

    except docker.errors.NotFound:
        raise HTTPException(status_code=404, detail="Container was not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Mistake: {str(e)}")
    

def config_edit(container_name: str, updated_content: str, file_path: str = "/etc/telegraf/telegraf.conf"):
    """This function edits the config file inside a container."""
    try:
        container = docker_client.containers.get(container_name)

        # creating temp file to store config in it
        temp_path = f"./{container_name}_updated.conf"
        with open(temp_path, "w", encoding="utf-8") as temp_file:
            temp_file.write(updated_content)

        # Creating tar-archieve with the config file
        tar_stream = BytesIO()
        with tarfile.open(fileobj=tar_stream, mode="w") as tar:
            tar.add(temp_path, arcname=os.path.basename(file_path))
        tar_stream.seek(0)

        # loading archive into container
        container.put_archive(
            os.path.dirname(file_path),
            tar_stream
        )
        # deelting temp file
        os.remove(temp_path)

        return {"update": "The configuration file was successfully updated"}

    except docker.errors.NotFound:
        raise HTTPException(status_code=404, detail="Container was not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Mistake: {str(e)}")


def delete_container(container_name: str):
    """This function deletes a container"""
    try:
        container = docker_client.containers.get(container_name)
        if container:
            container.stop()
            container.remove()
            return f"Container {container} was removed successfully"
        else:
            return f"Container {container} was not found. Check the name"
    except docker.errors.NotFound as e:
        raise HTTPException(status_code=500, detail=f"Docker error: {str(e)}") 
    

