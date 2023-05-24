from schemas.models import Student, Email
from scripts.db.mongo import myDB
from shortuuid import uuid
from tabulate import tabulate
from scripts.logging.logger import logger
from scripts.constants.app_constants import DBConstants, pipeline_aggregation
from scripts.utility.mongo_utility import MongoCollectionBaseClass


class Itemhandler:
    def __init__(self):
        self.user_mongo_obj = MongoCollectionBaseClass(database=DBConstants.DB_NAME,
                                                       collection=DBConstants.DB_COLLECTION)


def home():
    return {"This is for student registration into a course."}


def get_student():
    """
    what this guy is doing
    :return:
    """
    result = list(myDB.find({}))
    final_list = []
    for stud in result:
        del stud["_id"]
        final_list.append(stud)
    logger.info("Get the details of the student")
    return {"The data for all students ": final_list}


def insert_student(student: Student):
    student = student.dict()
    student["student_id"] = uuid()[:7]
    if not list(myDB.find({"roll": student["roll"]})):
        myDB.insert_one(student)
        logger.info("INFO: Adding a student detail ")
        return {"Success": "Added student in the course successfully"}
    else:
        logger.warning("Details of the student is not added")
        return {"Error": "Cannot add student, already enrolled in a course"}


def update_student(roll: int, student: Student):
    if not list(myDB.find({"roll": roll})):
        logger.warning("cannot update student details")
        return {"Error": "Student not enrolled in any course"}
    else:
        myDB.update_one({"roll": roll}, {"$set": student.dict()})
        logger.info("updated the students details")
        return {"Success": "Updated succesfully"}


def delete_student(roll: int):
    if not list(myDB.find({"roll": roll})):
        logger.info("The student details has been deleted succesfully")
        return {"Error": "Student has not enrolled in any course till now"}
    myDB.delete_one({"roll": roll})
    logger.info("Successfully deleted the student details")
    return {"Success": "Deleted the student from the course"}


def pipeline():
    data = myDB.aggregate(pipeline_aggregation.pipeline_agg)
    print(data)
    return list(data)[0]["total"]