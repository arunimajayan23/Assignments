from fastapi import APIRouter
from schemas.models import Student
from scripts.core.handlers.student_handler import get_student, insert_student, update_student, delete_student, pipeline
from scripts.core.handlers.email_handler import send_email, Email
from json2html import *
from scripts.constants.app_constants import *

app = APIRouter()


@app.get(APIs.view_all_items_api)
def show():
    try:
        return get_student()
    except Exception as e:
        print(e)
        return {"failed"}


@app.post(APIs.add_api)
def add(student: Student):
    try:
        return insert_student(student)
    except Exception as e:
        print(e)
        return {"failed"}


@app.put(APIs.update_api)
def update(roll: int, student: Student):
    try:
        return update_student(roll, student)
    except Exception as e:
        print(e)
        return {"failed"}


@app.delete(APIs.delete_api)
def delete(roll: int):
    try:
        return delete_student(roll)
    except Exception as e:
        print(e)
        return {"failed"}


@app.post(APIs.sent_api)
def fun(email: Email):
    try:
        all_billing_list_json = get_student()
        table = json2html.convert(json=all_billing_list_json)
        total_value = pipeline()
        message1 = f"Hello Sir/Madam <br><br>The table is:- {table}"
        message2 = f"{message1} \n total is {total_value}"
        send_email(message2, email)
        return {'message': 'email sent'}
    except Exception as e:
        print(e)
        return {"failed"}


@app.get(APIs.total_amount)
def fun():
    try:

        return pipeline()
    except Exception as e:
        print(e)
        return {"failed"}