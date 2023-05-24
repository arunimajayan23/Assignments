from pymongo import MongoClient
from scripts.constants.app_constants import *
from scripts.core.handlers.student_handler import *

client = MongoClient(DBConstants.DB_URI)
db = client[DBConstants.DB_NAME]
myDB = db[DBConstants.DB_COLLECTION]


def pipeline(pipeline: list):
    """Function to aggregate the items"""
    # logger.info("Mono_Query: pipeline_aggregation")
    return myDB.aggregate(pipeline)