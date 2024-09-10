# app/models.py
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Project(Base):
    __tablename__ = 'projects'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    client = Column(String, nullable=False)
    
    shifts = relationship("Shift", back_populates="project")
    invoices = relationship("Invoice", back_populates="project")

class Shift(Base):
    __tablename__ = 'shifts'
    
    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey('projects.id'), nullable=False)
    date = Column(DateTime, default=datetime.utcnow)
    hours_worked = Column(Float, nullable=False)
    
    project = relationship("Project", back_populates="shifts")

class Invoice(Base):
    __tablename__ = 'invoices'
    
    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey('projects.id'), nullable=False)
    total_hours = Column(Float, nullable=False)
    total_value = Column(Float, nullable=False)
    issued_date = Column(DateTime, default=datetime.utcnow)
    
    project = relationship("Project", back_populates="invoices")
