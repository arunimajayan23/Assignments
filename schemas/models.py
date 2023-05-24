from pydantic import BaseModel


class Student(BaseModel):
    name: str
    roll: int
    course: str
    course_fee: float


class Email(BaseModel):
    rec_email: str

