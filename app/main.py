from fastapi import FastAPI, HTTPException
from .utils import deserialize, serialize, create_docker_container, variables
from .models.upper_models import ConfigurationFile, SetAndStartConfigSchema


app = FastAPI()


@app.get("/get_config")
def get_config() -> ConfigurationFile:
    try:
        config_as_dict = deserialize(variables.CONFIGURATION_FILE_PATH)
        return ConfigurationFile(**config_as_dict)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/start_config")
def set_and_start_config(settings: SetAndStartConfigSchema):
    try:
        serialize(variables.CONFIGURATION_FILE_PATH, settings.config_update.model_dump())
        
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
    