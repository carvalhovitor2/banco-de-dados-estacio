# app/functions.py
from app.database import SessionLocal
from app.models import Project, Shift

# Function to add a new project
def add_project(name, client):
    session = SessionLocal()
    new_project = Project(name=name, client=client)
    session.add(new_project)
    session.commit()
    session.close()

# Function to add a new shift
def add_shift(project_id, hours_worked):
    session = SessionLocal()
    new_shift = Shift(project_id=project_id, hours_worked=hours_worked)
    session.add(new_shift)
    session.commit()
    session.close()

# Function to search for a project by name
def search_project(name):
    session = SessionLocal()
    project = session.query(Project).filter_by(name=name).first()
    session.close()
    return project

# Function to list all projects
def search_all_projects():
    session = SessionLocal()
    projects = session.query(Project).all()
    session.close()
    return projects

# Function to list all shifts for a project
def list_shifts(project_id):
    session = SessionLocal()
    shifts = session.query(Shift).filter_by(project_id=project_id).all()
    session.close()
    return shifts
