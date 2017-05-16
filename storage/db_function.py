#!/bin/usr/python3
'''
module contains functions related to the data
add_retweet
check_db_retweet
retrieve_retweets
'''
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import (sessionmaker, scoped_session)
from sqlalchemy.ext.declarative import declarative_base
from retweets import Base, Retweet

USER = 'root'
PWD = 'root'
DB = 'twitter_db'

class Tweet_db:
    def __init__(self):
        self.engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(USER, PWD, DB))
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        session = Session()

    def reload(self):
        Base.metadata.create_all(self.engine)
        self.session = scoped_session(sessionmaker(bind=self.engine,
                                                     expire_on_commit=False))

    def add_retweet(self, user, retweet):
        """
        arguements:

        user_id: twitter id of the user using the service
        retweet: the retweet obj
        """
        # insert retweet using mysqlalchmeny
        retweet = Retweet()
        retweet.user_id=user._json['id_str']
        retweet.user_email=user.email
        retweet.keyword=retweet.keyword
        retweet.tweet_id=retweet.tweet_id
        retweet.screen_name=retweet.screen_name
        retweet.text=retweet.text

        self.session.add(retweet)
        self.session.commit()


    def check_retweet(self, retweet_id):
        """
        arguements:

        retweet_id: id of the retweet
        returns True if retweet if found, False other wise
        """
        print("enter the function")
        session = self.session
        q = session.query(Retweet).filter(Retweet.tweet_id=retweet_id).all()
        if len(q) >= 1:
            return True
        else:
            return False


    def get_retweets(self, user_id):
        """
        arugements:

        user_id: twitter id of the user using the service

        Returns: an object of the retweets from the database
        """
        # get the tweet base on the user id
        pass
