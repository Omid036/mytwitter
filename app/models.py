from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime
from app.database import Base
from sqlalchemy.orm import relationship

class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    username = Column(
        String,
        unique=True,
        nullable=False
    )

    tweets = relationship(
        "Tweet",
        back_populates="user"
    )


class Tweet(Base):

    __tablename__ = "tweets"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    content = Column(
        String,
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    user = relationship(
        "User",
        back_populates="tweets"
    )


class Like(Base):

    __tablename__ = "likes"

    id = Column(Integer, primary_key=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    tweet_id = Column(
        Integer,
        ForeignKey("tweets.id")
    )


class Retweet(Base):

    __tablename__ = "retweets"

    id = Column(Integer, primary_key=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    tweet_id = Column(
        Integer,
        ForeignKey("tweets.id")
    )
