from fastapi import FastAPI
from .models.upper_models import ConfigSchema
from .docker_operations import docker_client


app = FastAPI()


@app.get("/get_all_containers")
def get_all_containers():
    return docker_client.get_all_containers()


@app.get("/get_config_file/{container_name}")
def get_container_config(container_name):
    return docker_client.get_container_config(container_name=container_name)


@app.post("/edit_config")
def edit_container_config(settings: ConfigSchema):
    return docker_client.edit_config(container_name=settings.container_name, 
                                     updated_config=settings.config)


@app.post("/create_new_container")
def create_new_container(settings: ConfigSchema) -> dict:
    return docker_client.create_new_container(container_name=settings.container_name, 
                                              config=settings.config)
    

@app.delete("/del_container/{container_name}")
def del_container(container_name: str) -> dict:
    return docker_client.delete_container(container_name=container_name)


@app.get("/get_stats")
def get_all_statistics():
    return docker_client.get_all_containers_statistics()

@app.get("/get_stats/{container_name}")
def get_statistics(container_name: str):
    return docker_client.get_container_statistics(container_name)


@app.get("/get_logs/{container_name}")
def get_container_logs(container_name: str):
    return {"logs": docker_client.get_logs(container_name)}
    