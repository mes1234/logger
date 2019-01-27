from sqlCreateDB import Project, Item, User, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime


engine = create_engine('sqlite:///dbStorage.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()
users = [
    {
        "name": "Witek",
        "password": "1234",
        "root": True,
    },
    {
        "name": "Ania",
        "password": "12344",
        "root": False,
    },
    {
        "name": "Artur",
        "password": "12fdf34",
        "root": False,
    },
]
# Insert a users in the person table
for user in users:
    session.add(User(**user))


project = Project(name="test1", description="fsdfsdfsdfs", owner_id=1)
session.add(project)

items = [
    {
        "project_id": 1,
        "name": "test1",
        "description": "ttest1",
        "date": datetime.now(),
        "owner_id": 1
    },
    {
        "project_id": 1,
        "name": "test2",
        "description": "ttest2",
        "date": datetime.now(),
        "owner_id": 3
    },
    {
        "project_id": 2,
        "name": "test3",
        "description": "ttest3",
        "date": datetime.now(),
        "owner_id": 3
    },
    {
        "project_id": 1,
        "name": "test4",
        "description": "ttest4",
        "date": datetime.now(),
        "owner_id": 2
    },
    {
        "project_id": 3,
        "name": "test44",
        "description": "ttest44",
        "date": datetime.now(),
        "owner_id": 2
    },
]
for item in items:
    session.add(Item(**item))
session.commit()
