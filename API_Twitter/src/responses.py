from pydantic import BaseModel


class TweetText(BaseModel):
    id: int
    text: str