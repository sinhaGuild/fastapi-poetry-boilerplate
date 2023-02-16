from sqlalchemy.orm import Session
from ..models import book
from . import schema


#   Get all books
def get_all_books(db: Session, skip: int = 0, limit: int = 100):
    return db.query(schema.Book).offset(skip).limit(limit).all()

#   Get a Single Book
def get_single_book(db:Session, book_id: int):
    return db.query(schema.Book).filter(schema.Book.id == book_id).first()

#   Create a single Book
# **book.dict() = convert to dict and pass as key:value pairs (**)
def create_book(db: Session, book: book.BookCreate):
    new_book = schema.Book(**book.dict())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book


# Delete a single book

# Update a single book