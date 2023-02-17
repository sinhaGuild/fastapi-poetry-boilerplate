from fastapi import FastAPI, Request
from .routers import books
import uvicorn
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

# build absolute paths
parent_dir_path = os.path.dirname(os.path.realpath(__file__))
static_dir_path = parent_dir_path+'/static'
template_dir_path = parent_dir_path+'/templates'

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
app.mount("/static", StaticFiles(directory=static_dir_path), name='static')
templates = Jinja2Templates(directory=template_dir_path)

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
        port=80, 
        reload=False
    )