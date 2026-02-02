from enum import Enum

class BookCategory(str, Enum):
    FICTION = "fiction"
    NONFICTION = "nonfiction"
    SCIENCE = "science"
    HISTORY = "history"
    BIOGRAPHY = "biography"
    TECHNOLOGY = "technology"
    OTHER = "other"

class Gender(str, Enum):
    MALE = "male"
    FEMALE = "female"
