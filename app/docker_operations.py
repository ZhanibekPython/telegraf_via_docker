import os
import subprocess
import docker
from fastapi import HTTPException
from docker.errors import NotFound, DockerException

from .utils import deserialize, serialize, variables



class DockerOperations:

    def __init__(self):
        try:
            self.docker_client = docker.from_env()
        except docker.errors.DockerException as e:
            raise HTTPException(status_code=500, detail=f"Failed to initialize Docker client: {str(e)}")


    def get_all_containers(self):
        """This method retrieves all created containers and their statuses"""
        try:
            all_containers = {}
            running = []
            exited = []
            paused = []
            restarting = []

            for container in self.docker_client.containers.list(all=True):
                all_containers[container.name] = container.status
                if container.status == "running":
                    running.append(container.name)
                elif container.status == "exited":
                    exited.append(container.name)
                elif container.status == "paused":
                    paused.append(container.name)
                elif container.status == "restarting":
                    restarting.append(container.name)

            return {
                "containers": all_containers,
                "running": running,
                "exited": exited,
                "paused": paused,
                "restarting": restarting,
            }

        except docker.errors.DockerException as e:
            raise HTTPException(status_code=500, detail=f"Docker error: {str(e)}")
        

    def delete_container(self, container_name: str):
        """This method removes a container by given name"""
        try:
            container = self.docker_client.containers.get(container_name)
            if container:
                container.stop()
                container.remove()
            if os.path.exists(self.get_config_path(container_name=container_name)):
                os.remove(self.get_config_path(container_name=container_name))

            return {"message": f"Container '{container_name}' was removed successfully"}
        except NotFound:
            raise HTTPException(status_code=404, detail=f"Container '{container_name}' not found")
        except DockerException as e:
            raise HTTPException(status_code=500, detail=f"Docker error: {str(e)}") 


    def get_container_config(self, container_name: str, file_path: str = "/etc/telegraf/telegraf.conf") -> dict:
        """
        Retrieves, deserializes, and validates the config file from a container via Docker CLI.
        :param container_name: Name of the container.
        :param file_path: Path to the configuration file inside the container.
        :return: Validated content of the configuration file.
        """
        try:
            temp_file_path = os.path.join(os.getcwd(), "app", "temp_files", f"{container_name}.conf")
            os.makedirs(os.path.dirname(temp_file_path), exist_ok=True)
            print(temp_file_path)
            command = ["docker", "cp", f"{container_name}:{file_path}", temp_file_path]

            result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if result.returncode != 0:
                raise HTTPException(status_code=404, detail=f"Failed to copy file. Error: {result.stderr.strip()}")

            deserialized_content = deserialize(temp_file_path, file=True)

            os.remove(temp_file_path)

            return deserialized_content.model_dump(exclude_unset=True)

        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")


    def create_docker_container(
        self, 
        new_container_name: str, 
        what_to_mount: str,
        docker_image_name: str = variables.TELEGRAF_IMAGE, 
        where_to_mount: str = "/etc/telegraf/telegraf.conf"
    ) -> str:
        """This method creates a new Docker container with the specified image and volume presetting"""

        try:
            command = [
                "docker", "run", "-d", "--name", new_container_name,
                "-v", f"{what_to_mount}:{where_to_mount}:rw",
                "-e", f"TELEGRAF_CONFIG_PATH={where_to_mount}",
                docker_image_name
            ]
            
            result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

            if result.returncode != 0:
                raise HTTPException(status_code=500, detail=f"Failed to create container. Error: {result.stderr.strip()}")

            return result.stdout.strip()

        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")


    def get_config_path(self, container_name: str) -> str:
        """
        This method returns the expected configuration file path for the given container name.
        
        :param container_name: The name of the container
        :return: The absolute path to the config file.
        """
        try:
            file_name = f"{container_name}.conf"
            config_path = os.path.join(os.getcwd(), "app", "active_containers", file_name)
            return config_path

        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error generating configuration path: {str(e)}")


    def create_new_container(self, container_name: str, config: dict) -> dict:
        """
        This method creates a new Docker container using a provided configuration.

        :param container_name: The name of the new container.
        :param config: The configuration data (ConfigurationFile instance).
        :return: A dictionary with the creation message or raises an HTTPException on error.
        """
        try:
            config_path = self.get_config_path(container_name)

            directory = os.path.dirname(config_path)
            if not os.path.exists(directory):
                os.makedirs(directory, exist_ok=True)

            serialize(config, save_to_file=True, filename=config_path)

            container_id = self.create_docker_container(
                new_container_name=container_name,
                what_to_mount=config_path,
            )

            return {
                "message": f"New container {container_name} was created.",
                "container_id": container_id,
            }

        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Server error: {str(e)}")


    def edit_config(self, container_name: str, updated_config: dict):
        """Update configuration file inside a Docker container with validation"""

        try:
            container = self.docker_client.containers.get(container_name)
            if container:
                container.stop()
                container.remove()
            else:
                return {"message": f"Container {container_name} was not found"}

            config_path = self.get_config_path(container_name)

            directory = os.path.dirname(config_path)
            if not os.path.exists(directory):
                os.makedirs(directory, exist_ok=True)

            if os.path.exists(config_path):
                os.remove(config_path)

            serialize(updated_config, save_to_file=True, filename=config_path)

            self.create_docker_container(new_container_name=container_name, what_to_mount=config_path)

            return {"update": "Configuration file successfully updated"}

        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")   


    def get_logs(self, container_name: str) -> str:
        """
        This method retrieves logs for specified container
        
        :param container_name: Enter container name, you would like to get logs from.
        :return: Str-typed logs.
        """
        try:
            container = self.docker_client.containers.get(container_name)
            logs = container.logs(tail=30).decode('utf-8')
            return logs
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error retrieving logs for container '{container_name}': {str(e)}")


    def get_all_containers_statistics(self) -> dict:
        """
        This method retrieves stats for all containers. No stream.
        
        :return: Dict-typed stats for all containers.
        """
        try:
            containers = self.docker_client.containers.list(all=True)

            stats = {}

            for container in containers:
                container_name = container.name
                container_stats = container.stats(stream=False)

                stats[container_name] = {
                    "cpu_usage": container_stats["cpu_stats"]["cpu_usage"]["total_usage"],
                    "memory_usage": container_stats["memory_stats"]["usage"],
                    "memory_limit": container_stats["memory_stats"]["limit"],
                    "network_rx_bytes": sum(net["rx_bytes"] for net in container_stats["networks"].values()),
                    "network_tx_bytes": sum(net["tx_bytes"] for net in container_stats["networks"].values()),
                }

            return stats

        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error retrieving statistics for all containers: {str(e)}")


    def get_container_statistics(self, container_name: str) -> dict:
        """
        Retrieves container statistics.
        
        :param container_name: Contianer name.
        :return: Dict-typed container stats.
        """
        try:
            container = self.docker_client.containers.get(container_name)
            stats = container.stats(stream=False)
            return stats

        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error retrieving statistics for container '{container_name}': {str(e)}")
        

docker_client = DockerOperations()