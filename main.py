from typing import List

from pydantic import BaseModel

from fastapi import FastAPI, HTTPException

app = FastAPI()


users = [
    {
        "id": 1,
        "username": "johndoe",
        "email": "something@example.com",
    },
    {
        "id": 2,
        "username": "joeappleseed",
        "email": "john@example.com",
    }
]

followers = [
    {
        "id": 1,
        "user_id": 1,
        "follower_id": 2,
    }
]

tweets = [
    {
        "id": 1,
        "user_id": 1,
        "text": "This is a tweet",
    },
    {
        "id": 2,
        "user_id": 1,
        "text": "I like big butts and I cannot lie",
    },
    {
        "id": 3,
        "user_id": 2,
        "text": "This is another tweet",
    },
]

class TweetCreate(BaseModel):
    user_id: int
    text: str

class Tweet(BaseModel):
    id: int
    user_id: int
    text: str

class UserCreate(BaseModel):
    username: str
    email: str

class User(BaseModel):
    id: int
    username: str
    email: str

@app.get("/tweet/{tweet_id}", status_code=200, response_model=Tweet)
async def get_tweet(tweet_id: int):
    result = [tweet for tweet in tweets if tweet["id"] == tweet_id]
    if not result:
        raise HTTPException(status_code=404, detail="Tweet not found")

    return result[0]

@app.get("/user/{user_id}/tweets", status_code=200, response_model=List[Tweet])
async def get_tweets_by_user(user_id: int):
    return [tweet for tweet in tweets if tweet["user_id"] == user_id] 

@app.get("/user/{user_id}/followers", status_code=200, response_model=List[User])
async def get_followers(user_id: int):
    return [user for user in users if user["id"] in [
        follower["follower_id"] for follower in followers if follower["user_id"] == user_id]
    ]

@app.post("/tweet", status_code=201, response_model=Tweet)
async def create_tweet(tweet_in: TweetCreate):
    tweet = {
        "id": len(tweets) + 1,
        "user_id": tweet_in.user_id,
        "text": tweet_in.text,
    }
    tweets.append(tweet)
    return tweet
