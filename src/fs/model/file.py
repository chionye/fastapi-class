from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from fs.config.database import Base

class File(Base):
   __tablename__ = "files"

    id = Column(Integer, primary_key=True, index=True)
    original_name = Column(String(255), nullable=False)
    stored_name = Column(String(255), nullable=True)
    content_type = Column(String(255), nullable=True)
    size = Column(Integer, nullable=True)
    url = Column(String(500), nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

class FileResponse(BaseModel):
    id: int
    original_name: str
    content_type: str
    size: int
    url: str
    created_at: datetime

    class Config:
        from_attributes = True