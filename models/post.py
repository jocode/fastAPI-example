from pydantic import BaseModel
from typing import Text, Optional
from datetime import datetime

class Post(BaseModel):
    id: Optional[str]
    title: str
    content: Text
    author: str
    created_at: datetime = datetime.now()
    published_at: Optional[datetime]
    published: bool = False