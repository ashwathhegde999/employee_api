# this is the comment

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Data model
class Employee(BaseModel):
    id: int
    name: str
    role: str

# In-memory database
employees_db = [
    {"id": 1, "name": "Alice Smith", "role": "Software Engineer"},
    {"id": 2, "name": "Bob Jones", "role": "Data Scientist"}
]

@app.get("/employees")
def get_employees():
    return employees_db

@app.post("/employees")
def add_employee(emp: Employee):
    employees_db.append(emp.model_dump())
    return emp

@app.get("/health")
def health():
    return {"status": "ok", "version": "2.0"}
