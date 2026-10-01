# Employee Microservices Demo

A simple Employee Management System built using **Python, FastAPI, SQLAlchemy, SQLite, and Microservices Architecture**.

## Project Overview

This project demonstrates how multiple independent microservices communicate with each other through REST APIs.

### Microservices

- **Employee Service** – Manages employee records
- **Department Service** – Manages department records
- **API Gateway** – Provides a single entry point to access the services

## Technologies Used

- Python
- FastAPI
- SQLAlchemy
- SQLite
- REST APIs
- HTTPX
- Swagger / OpenAPI
- Git & GitHub

## Architecture

```text
                Client
                  |
                  v
            API Gateway
              Port 8000
             /         \
            /           \
           v             v
 Employee Service    Department Service
   Port 8001            Port 8002
      |                    |
      v                    v
 employee.db          department.db    