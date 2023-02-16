from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from enum import Enum
from pydantic import BaseModel
from ..models.book import Book, Category, BookSelection
from ..database.schema import Base, engine, SessionLocal
from ..database import crud

router = APIRouter()

#   connect sqlalchemy models
Base.metadata.create_all(bind=engine)

# db readiness dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# books = {
#     0: Book(id=0, title="The Maid", author="Nita Prose", price="10.99", category=Category.FICTION),
#     1: Book(id=1, title="The House of Sky and Breath", author="Sarah J Mass", price="13.99", category=Category.FICTION),
#     2: Book(id=2, title="Sea of Tranquility", author="Emily Mandel", price="13.99", category=Category.SCIENCEFICTION),
#     3: Book(id=3, title="Book Lovers", author="Emily Henry", price="9.99", category=Category.NONFICTION),
#     }




#   Query a book with id
@router.get("/{book_id}")
async def get_book_by_id(book_id: int, db:Session = Depends(get_db)) -> Book:
    single_book = crud.get_single_book(db=db, book_id=book_id)
    
    if single_book is None:
        raise HTTPException(status_code=404, detail=f"Book with {book_id} does not exist!")

    return single_book    
    # if book_id not in books:
    #     HTTPException(status_code=404, detail=f"Book with {book_id} does not exist!")
    # return books[book_id]

#   Query a book with all model parameters
@router.get("/")
async def query_book_with_parameters(
    title: str | None = None,
    author: str | None = None,
    price: float | None = None,
    category: Category | None = None,
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    def check_book(book: Book):
        """Check if the book matches the query arguments from the outer scope."""
        return all(
            (
                title is None or book.title == title,
                price is None or book.price == price,
                author is None or book.author == author,
                category is None or book.category is category,
            )
        )
    f_books = crud.get_all_books(db, skip=skip, limit=limit)
    selection = [book for book in f_books if check_book(book)]
    return {
        "query": {"title": title, "price": price, "author": author, "category": category},
        "selection": selection,
    }

#   Get all Books
@router.get("/all/books")
async def get_all_books(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    f_books = crud.get_all_books(db, skip=skip, limit=limit)
    return {"books": f_books}

# @router.get("/all/books", response_model=list[Book])
# async def get_all_books() -> dict[str, dict[int, Book]]:
#     return {"books": books}


#   Add a Book
@router.post("/")
async def add_book(book: Book, db: Session = Depends(get_db)):
    return crud.create_book(db=db, book=book)

# #   Add a Book
# @router.post("/")
# async def add_book(book: Book) -> dict[str, Book]:
#     if book.id in books:
#         HTTPException(status_code=400, detail=f"Book with {book.id=} already exists.")

#     books[book.id] = book
#     return {"added": book}


#   Delete a Book
@router.delete("/{book_id}")
async def delete_book_by_Id(book_id: int, db: Session = Depends(get_db)) -> dict[str, Book]:
    single_book = crud.get_single_book(db=db, book_id=book_id)
    
    if single_book is None:
        raise HTTPException(status_code=404, detail=f"Book with {book_id} does not exist!")

    return {"message": "Method Not Yet implemented!"} 

    # if book_id not in books:
    #     raise HTTPException(
    #         status_code=404, detail=f"Book with {book_id=} does not exist."
    #     )

    # book = books.pop(book_id)
    # return {"deleted": book}

# Update a Book by Id
@router.put("/{book_id}")
async def update_book_by_Id(
    book_id: int,
    title: str | None = None,
    author: str | None = None,
    price: float | None = None,
    category: Category | None = None,
):
    # if book_id not in books:
    #     HTTPException(status_code=404, detail=f"Book with {book_id=} does not exist.")
    # if all(info is None for info in (title, author, price, category)):
    #     raise HTTPException(
    #         status_code=400, detail="No parameters provided for update."
    #     )

    # book = books[book_id]
    # if title is not None:
    #     book.title = title
    # if price is not None:
    #     book.price = price
    # if author is not None:
    #     book.author = author
    # if category is not None:
    #     book.category = category
    
    return {"message": "Method Not Yet implemented!"} 
    # return {"updated": book}