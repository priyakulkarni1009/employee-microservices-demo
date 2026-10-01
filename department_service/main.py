from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from .database import engine, Base, get_db
from . import models

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Department Service API",
    description="Department Management Microservice",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Department Service is running!"
    }


@app.get("/api/departments")
def get_departments(db: Session = Depends(get_db)):
    departments = db.query(models.Department).all()
    return departments    
@app.post("/api/departments")
def create_department(
    name: str,
    location: str,
    db: Session = Depends(get_db)
):
    new_department = models.Department(
        name=name,
        location=location
    )

    db.add(new_department)
    db.commit()
    db.refresh(new_department)

    return new_department   
@app.put("/api/departments/{department_id}")
def update_department(
    department_id: int,
    name: str,
    location: str,
    db: Session = Depends(get_db)
):
    department = db.query(models.Department).filter(
        models.Department.id == department_id
    ).first()

    if department is None:
        return {"message": "Department not found"}

    department.name = name
    department.location = location

    db.commit()
    db.refresh(department)

    return department     
@app.delete("/api/departments/{department_id}")
def delete_department(
    department_id: int,
    db: Session = Depends(get_db)
):
    department = db.query(models.Department).filter(
        models.Department.id == department_id
    ).first()

    if department is None:
        return {"message": "Department not found"}

    db.delete(department)
    db.commit()

    return {
        "message": "Department deleted successfully"
    }      