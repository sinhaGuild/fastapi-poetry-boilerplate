from enum import Enum
from pydantic import BaseModel


class Category(Enum):
    FICTION = "fiction"
    NONFICTION="non-fiction"
    SCIENCEFICTION="science-fiction"

class Book(BaseModel):
    title: str
    author: str
    price: float
    id: int
    category: Category
    class Config:
        orm_mode = True

class BookBase(BaseModel):
    id: int
    title: str
    author: str
    price: float = 1.99
    category: Category = Category.NONFICTION

class BookCreate(BookBase):
    pass

# users query arguments
BookSelection = dict[str, str | str | float | int | Category | None]