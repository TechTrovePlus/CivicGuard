from app.db.base import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

class ScanJob(Base):
    __tablename__ ="scan_jobs"

    id = Column(Integer, primary_key=True)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False) #one User -> many scanjobs; users is parent & scanjob is child; child will reference parent
    target = Column(String, nullable=False)
    scan_type = Column(String, nullable=False)
    status = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    owner = relationship(
        "User",
        back_populates="scans"
        )