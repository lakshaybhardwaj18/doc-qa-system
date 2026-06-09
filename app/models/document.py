from sqlalchemy import Column, String , JSON
from sqlalchemy.sql import func
from app.database import Base
import uuid
class Document(Base):
    __tablename__="documents"
    id= Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    title=Column(String, nullable=False)
    content=Column(String,nullable=False)
    tags=Column(JSON, default=[])
    created_at=Column(String, default=func.now())
    owner_id = Column(String, nullable=False)