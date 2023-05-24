import uvicorn
from fastapi import FastAPI
from scripts.core.services.services_student import app as student_id
from scripts.constants.app_configurations import *
from scripts.logging.logger import logger

app_main = FastAPI()

app_main.include_router(student_id)

if __name__ == "__main__":
    # logger.info("Service started in {host_name}:{port}".format(host_name=SERVICE_HOST, port=SERVICE_PORT))
    logger.info("Service started")
    uvicorn.run("main:app_main", host=SERVICE_HOST, port=int(SERVICE_PORT), reload=True)
    logger.info("Service stopped")