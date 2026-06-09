from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from dotenv import load_dotenv
import os
load_dotenv()
#engine=connection to db
DATABASE_URL=os.getenv("DATABASE_URL")
engine=create_engine(DATABASE_URL)
#session = conversation with db
SessionLocal=sessionmaker(bind=engine)
#base=parent for all your db models
class Base(DeclarativeBase):
    pass
#Dependency-FastAPI will call this to get a DB session per request
def get_db():
    db=SessionLocal()
    try:
        yield db #give the session to the route
    finally: 
        db.close() # always close after request is done