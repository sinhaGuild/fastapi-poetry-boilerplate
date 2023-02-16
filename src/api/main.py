from fastapi import FastAPI, Request
from .routers import books
import uvicorn
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# instantiate app
app = FastAPI(
    swagger_ui_parameters={
        "syntaxHighlight.theme": "arta",
        "displayRequestDuration": True,
        "showCommonExtensions": True,
        "tryItOutEnabled": True,
        "deepLinking": True,

        }
)

# mount static files and templates
app.mount("/static", StaticFiles(directory="static"), name='static')
templates = Jinja2Templates(directory="templates")

#   Home page
@app.get("/", response_class=HTMLResponse)
async def home_page(request: Request):
    return templates.TemplateResponse("homepage.html", {"request": request})


# include routes
app.include_router(
    books.router,
    prefix="/books",
    tags=["Books"],
    responses={404: {"description": "Not found!"}, 418: {"description": "I'm a teapot!"}},
)


# scripts for poetry: development
def dev():
    uvicorn.run(
        "api.main:app", 
        host="0.0.0.0", 
        port=8000, 
        reload=True
    )

# scripts for poetry: production
def start():
    uvicorn.run(
        "api.main:app", 
        host="0.0.0.0", 
        port=8000, 
        reload=False
    )