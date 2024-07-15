from pydantic import BaseModel, Field
from typing import Optional

class TDocument(BaseModel):
    url: str
    pub_date: int
    fetch_time: int
    text: str
    first_fetch_time: Optional[int] = Field(default=None)


