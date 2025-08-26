import os

import docker
from docker.errors import DockerException
from fastapi import HTTPException


def run_spark_job_container() -> dict:
    try:
        client = docker.from_env()
        image_name = "pulse-analytics-spark-job:latest"
        network_name = "pulse-analytics_default"

        host_project_path = os.getenv("HOST_PROJECT_PATH")
        if not host_project_path:
            raise ValueError("HOST_PROJECT_PATH environment variable not set.")

        host_data_path = os.path.join(host_project_path, "data")
        container_data_path = "/app_data"

        print(f"Attempting to run container from image: {image_name}")
        print(
            f"Mounting host path '{host_data_path}' to container "
            f"path '{container_data_path}'"
        )

        container = client.containers.run(
            image=image_name,
            detach=True,
            network=network_name,
            auto_remove=True,
            volumes={host_data_path: {"bind": container_data_path, "mode": "ro"}},
        )

        print(f"Successfully started container: {container.id}")
        return {
            "message": "Spark job container started successfully.",
            "container_id": container.id,
        }

    except DockerException as e:
        print(f"Error interacting with Docker daemon: {e}")
        raise HTTPException(
            status_code=500, detail=f"Error starting Spark job container: {e}"
        )
