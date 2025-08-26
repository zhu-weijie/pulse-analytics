import docker
from docker.errors import DockerException
from fastapi import HTTPException


def run_spark_job_container() -> dict:
    try:
        client = docker.from_env()
        image_name = "pulse-analytics-spark-job:latest"
        network_name = "pulse-analytics_default"

        print(f"Attempting to run container from image: {image_name}")

        container = client.containers.run(
            image=image_name,
            detach=True,
            network=network_name,
            auto_remove=True,
            volumes={"/app_data": {"bind": "/app_data", "mode": "ro"}},
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
