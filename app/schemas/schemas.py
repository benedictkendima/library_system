from pydantic import BaseModel
from enums import BookCategory
from datetime import date
from typing import List, Optional, Dict



class BookCreate(BaseModel):
    title: str
    author: str
    category: BookCategory
    published_date: date