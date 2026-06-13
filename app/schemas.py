from pydantic import BaseModel
from datetime import datetime


class TweetCreate(BaseModel):
    content: str


class TweetResponse(BaseModel):
    id: int
    content: str
    created_at: datetime

    class Config:
        from_attributes = True
