from fastapi import APIRouter, BackgroundTasks

from pulse_analytics.jobs.trigger import run_spark_job_container

router = APIRouter(
    prefix="/jobs",
    tags=["jobs"],
)


@router.post("/trigger/transform", status_code=202)
def trigger_transform_job(background_tasks: BackgroundTasks):
    background_tasks.add_task(run_spark_job_container)

    return {"message": "Accepted: Spark transformation job trigger has been received."}
