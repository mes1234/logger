import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Project(Base):
    '''
    table to store all projects within system
    '''
    __tablename__ = 'projects'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(1000), nullable=False)
    owner_id = Column(Integer, ForeignKey('users.id'))
    # users_id ? TODO


class Item(Base):
    '''
    class to store items in db
    '''
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey('projects.id'))
    name = Column(String(250), nullable=False)
    description = Column(String(1000), nullable=False)
    date = Column(DateTime(timezone=False), nullable=False)
    owner_id = Column(Integer, ForeignKey('users.id'))


class User(Base):
    '''
    class definition to store users table
    '''
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    root = Column(Boolean, nullable=False)


# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine('sqlite:///dbStorage.db')

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)
