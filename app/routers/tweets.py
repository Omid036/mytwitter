from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Tweet
from app.schemas import TweetCreate
from app.schemas import TweetResponse

router = APIRouter(tags=["Tweets"])


@router.post("/tweets", response_model=TweetResponse)
def create_tweet(
    tweet: TweetCreate,
    db: Session = Depends(get_db)
):
    new_tweet = Tweet(
        content=tweet.content
    )

    db.add(new_tweet)
    db.commit()
    db.refresh(new_tweet)

    return new_tweet


@router.get(
    "/tweets",
    response_model=list[TweetResponse]
)
def get_tweets(
    db: Session = Depends(get_db)
):
    return db.query(Tweet).all()


@router.get(
    "/tweets/{tweet_id}",
    response_model=TweetResponse
)
def get_tweet(
    tweet_id: int,
    db: Session = Depends(get_db)
):

    tweet = (
        db.query(Tweet)
        .filter(Tweet.id == tweet_id)
        .first()
    )

    if not tweet:
        raise HTTPException(
            status_code=404,
            detail="Tweet not found"
        )

    return tweet


@router.delete("/tweets/{tweet_id}")
def delete_tweet(
    tweet_id: int,
    db: Session = Depends(get_db)
):

    tweet = (
        db.query(Tweet)
        .filter(Tweet.id == tweet_id)
        .first()
    )

    if not tweet:
        raise HTTPException(
            status_code=404,
            detail="Tweet not found"
        )

    db.delete(tweet)
    db.commit()

    return {
        "message": "Tweet deleted"
    }
