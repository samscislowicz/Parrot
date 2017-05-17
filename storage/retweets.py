from datetime import datetime
import uuid
from sqlalchemy import Column, Integer, String, Table, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
xoimport uuid


Base = declarative_base()
class Retweet(Base):
    __tablename__ = "retweets"
    id = Column(String(60), primary_key=True, nullable=False)
    user_id = Column(String(250), nullable=True)
    user_email = Column(String(250), nullable=True)
    keyword = Column(String(250), nullable=True)
    tweet_id = Column(String(250), nullable=True)
    screen_name = Column(String(128), nullable=True)
    created_at = Column(DateTime(timezone=True), default=datetime.now(), nullable=False)
    text = Column(Text, nullable=True)
