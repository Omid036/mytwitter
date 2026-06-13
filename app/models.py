from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.database import Base


class Tweet(Base):

    __tablename__ = "tweets"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
