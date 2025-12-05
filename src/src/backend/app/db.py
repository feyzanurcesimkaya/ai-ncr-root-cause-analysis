from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()


class NCRModel(Base):
    __tablename__ = "ncr"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    project = Column(String(255), nullable=False)
    location = Column(String(255), nullable=False)
    discipline = Column(String(100), nullable=False)
    severity = Column(String(10), nullable=False)
    status = Column(String(20), default="open")
    created_at = Column(DateTime, default=datetime.utcnow)
    root_cause = Column(Text, nullable=True)
