from fastapi import FastAPI
import httpx
import os
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

EMPLOYEE_SERVICE_URL = os.getenv("EMPLOYEE_SERVICE_URL")
DEPARTMENT_SERVICE_URL = os.getenv("DEPARTMENT_SERVICE_URL")

app = FastAPI(
    title="API Gateway",
    description="API Gateway for Employee and Department Microservices",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "API Gateway is running!"
    }


@app.get("/api/employees")
def get_employees():
    response = httpx.get(
        f"{EMPLOYEE_SERVICE_URL}/api/employees"
    )
    return response.json()


@app.get("/api/departments")
def get_departments():
    response = httpx.get(
        f"{DEPARTMENT_SERVICE_URL}/api/departments"
    )
    return response.json()  