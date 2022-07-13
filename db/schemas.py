from pydantic import BaseModel


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