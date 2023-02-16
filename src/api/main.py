from fastapi import FastAPI
from .routers import books
import uvicorn

app = FastAPI()

# include routes
app.include_router(
    books.router,
    prefix="/books",
    tags=["books"],
    responses={404: {"description": "Not found!"}, 418: {"description": "I'm a teapot!"}},
)


# scripts for poetry
def dev():
    uvicorn.run(
        "src.api.main:app", 
        host="0.0.0.0", 
        port=8000, 
        reload=True
    )

def start():
    uvicorn.run(
        "src.api.main:app", 
        host="0.0.0.0", 
        port=8000, 
        reload=False
    )