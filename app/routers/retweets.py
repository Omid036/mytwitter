from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Retweet

router = APIRouter(tags=["Retweets"])


@router.post("/tweets/{tweet_id}/retweet")
def retweet_tweet(
    tweet_id: int,
    db: Session = Depends(get_db)
):

    retweet = Retweet(
        user_id=1,
        tweet_id=tweet_id
    )

    db.add(retweet)
    db.commit()

    return {
        "message": "retweeted"
    }


@router.delete("/tweets/{tweet_id}/retweet")
def delete_retweet(
    tweet_id: int,
    db: Session = Depends(get_db)
):

    retweet = (
        db.query(Retweet)
        .filter(
            Retweet.user_id == 1,
            Retweet.tweet_id == tweet_id
        )
        .first()
    )

    if retweet:
        db.delete(retweet)
        db.commit()

    return {
        "message": "retweet removed"
    }
