from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import httpx 
from .database import engine, Base, get_db
from . import models
from .schemas import EmployeeCreate

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Employee Service API",
    description="Employee Management Microservice",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Employee Service is running!"
    }


@app.get("/api/employees")
def get_employees(db: Session = Depends(get_db)):
    employees = db.query(models.Employee).all()
    return employees 


@app.post("/api/employees")
def create_employee(
    employee: EmployeeCreate,
    db: Session = Depends(get_db)
):
    new_employee = models.Employee(
        name=employee.name,
        email=employee.email,
        designation=employee.designation,
        salary=employee.salary
    )

    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)

    return new_employee 
@app.put("/api/employees/{employee_id}")
def update_employee(
    employee_id: int,
    employee: EmployeeCreate,
    db: Session = Depends(get_db)
):
    existing_employee = db.query(models.Employee).filter(
        models.Employee.id == employee_id
    ).first()

    if existing_employee is None:
        return {"message": "Employee not found"}

    existing_employee.name = employee.name
    existing_employee.email = employee.email
    existing_employee.designation = employee.designation
    existing_employee.salary = employee.salary

    db.commit()
    db.refresh(existing_employee)

    return existing_employee 
@app.delete("/api/employees/{employee_id}")
def delete_employee(
    employee_id: int,
    db: Session = Depends(get_db)
):
    employee = db.query(models.Employee).filter(
        models.Employee.id == employee_id
    ).first()

    if employee is None:
        return {"message": "Employee not found"}

    db.delete(employee)
    db.commit()

    return {
        "message": "Employee deleted successfully"
    }         
@app.get("/api/employees/{employee_id}/department/{department_id}")
def get_employee_department(
    employee_id: int,
    department_id: int
):
    # First check that the employee exists
    employee_response = httpx.get(
        f"http://127.0.0.1:8001/api/employees"
    )

    employees = employee_response.json()

    employee = next(
        (emp for emp in employees if emp["id"] == employee_id),
        None
    )

    if employee is None:
        return {"message": "Employee not found"}

    # Call Department Service
    department_response = httpx.get(
        f"http://127.0.0.1:8002/api/departments"
    )

    departments = department_response.json()

    department = next(
        (dept for dept in departments if dept["id"] == department_id),
        None
    )

    if department is None:
        return {"message": "Department not found"}

    return {
        "employee": employee,
        "department": department
    }       