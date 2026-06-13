from fastapi import FastAPI

from app.database import Base, engine

from app.routers import tweets, likes, retweets
from app import models

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Twitter Clone API"}


app.include_router(tweets.router)
app.include_router(likes.router)
app.include_router(retweets.router)
