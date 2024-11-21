from fastapi import FastAPI, HTTPException
from .utils import deserialize, serialize, create_docker_container, variables, get_containers, config_edit, get_container_config, delete_container
from .models.upper_models import ConfigurationFile, SetAndStartConfigSchema, ConfigEdit


app = FastAPI()


@app.get("/containers")
def get_all_containers():
    return get_containers()


@app.get("/containers/{container_name}")
def get_config(container_name):
    return get_container_config(container_name=container_name)


@app.post("/edit_config")
def configurate_edit(data: ConfigEdit) -> dict:
    return config_edit(data.container_name, data.new_content)


@app.post("/start_config")
def start_new_config(settings: SetAndStartConfigSchema):
    try:
        serialize(variables.CONFIGURATION_FILE_PATH, settings.config_update.model_dump(exclude_unset=True))
        
        new_container_name = settings.new_docker_container_name

        container_id = create_docker_container(
            new_container_name=new_container_name,
            config_file_path=variables.CONFIGURATION_FILE_PATH
        )
        
        return {
            "message": f"Configuration file updated and new container '{new_container_name}' created",
            "container_id": container_id
        }
    except (OSError, ValueError) as e:
        raise HTTPException(status_code=500, detail=f"Server error: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@app.delete("/del_container/{container_name}")
def del_container(container_name: str) -> dict:
    result = delete_container(container_name=container_name)
    return {"result": result}