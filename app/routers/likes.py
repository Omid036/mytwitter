from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Like

router = APIRouter(tags=["Likes"])


@router.post("/tweets/{tweet_id}/like")
def like_tweet(
    tweet_id: int,
    db: Session = Depends(get_db)
):

    like = Like(
        user_id=1,
        tweet_id=tweet_id
    )

    db.add(like)
    db.commit()

    return {
        "message": "liked"
    }


@router.delete("/tweets/{tweet_id}/like")
def unlike_tweet(
    tweet_id: int,
    db: Session = Depends(get_db)
):

    like = (
        db.query(Like)
        .filter(
            Like.user_id == 1,
            Like.tweet_id == tweet_id
        )
        .first()
    )

    if like:
        db.delete(like)
        db.commit()

    return {
        "message": "unliked"
    }
