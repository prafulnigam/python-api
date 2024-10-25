from pydantic import BaseModel, Field
from typing import Optional

class Blog(BaseModel):
    title: str = Field(..., title="Title of the blog")
    content: str = Field(..., title="Content of the blog")
    author: str = Field(..., title="Author of the blog")
    published: Optional[bool] = Field(default=True, title="Is the blog published?")

    class Config:
        schema_extra = {
            "example": {
                "title": "My first blog",
                "content": "This is the content of the blog.",
                "author": "John Doe",
                "published": True
            }
        }
