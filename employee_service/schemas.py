from pydantic import BaseModel


class EmployeeCreate(BaseModel):
    name: str
    email: str
    designation: str
    salary: float 