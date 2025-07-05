#defines database models
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class WorkEntry(Base):
    __tablename__ = "work_entries"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True, nullable=False)
    entry = Column(String, nullable=False)
    polished_output = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    

