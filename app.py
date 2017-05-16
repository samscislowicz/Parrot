#!/usr/bin/python3

'''
flask-tweepy-oauth

derived from the following code: https://github.com/whichlight/flask-tweepy-oauth
'''

from flask import Flask
from flask import request
import flask
import tweepy
app = Flask(__name__)

CONSUMER_KEY = 'Qpm9g92Rm61ZDblY5wKvWCXnn'
CONSUMER_SECRET = 'parIwRKtMTNrN5qX5uMkTfiQ6yfW7tiwzPxtfi5a256r6tiB83'
CALLBACK_URL = 'http://127.0.0.1:5000/verify'
session = {}
db = {} #you can save these values to a database

@app.route("/")
def send_token():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET, CALLBACK_URL)
    try:
        # get the request tokens
        redirect_url = auth.get_authorization_url()
        session['request_token'] = auth.request_token
    except tweepy.TweepError:
        print('Error! Failed to get request token')
        #this is twitter's url for authentication
#        return flask.redirect(redirect_url)

@app.route("/verify")
def get_verification():
    #get the verifier key from the request url
    verifier = request.GET.get['oauth_verifier']
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    
    request_token = session.get('request_token')
    del session['request_token']
    auth.request_token = request_token

    try:
        auth.get_access_token(verifier)
    except tweepy.TweepError:
        print('Error! Failed to get access token.')
    # now you have access!
    api = tweepy.API(auth)
    # store in a db
    db['api'] = api
    db['access_token_key'] = auth.access_token.key
    db['access_token_secret'] = auth.access_token.secret
    return flask.redirect(flask.url_for('start'))

@app.route("/start")
def start():
    # auth done, app logic can begin
    api = db['api']
    # example, print your latest status posts
    return flask.render_template('tweets.html', tweets=api.user_timeline())

if __name__ == "__main__":
    app.run()
