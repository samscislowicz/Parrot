-- Create Twitter db
CREATE DATABASE IF NOT EXISTS twitter_db;
USE twitter_db;
CREATE TABLE IF NOT EXISTS retweets (
id int(11) NOT NULL AUTO_INCREMENT,
user_id varchar(250)    DEFAULT    NULL,
tweet_id varchar(250)    DEFAULT    NULL,
screen_name varchar(128) DEFAULT NULL,
created_at timestamp NULL DEFAULT NULL,
text text,
PRIMARY KEY (id)
) AUTO_INCREMENT=56 DEFAULT CHARSET=utf8;
