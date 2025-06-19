from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/page1", response_class=HTMLResponse)
async def page1(request: Request):
    return templates.TemplateResponse("page1.html", {"request": request})

@app.get("/page2", response_class=HTMLResponse)
async def page2(request: Request):
    return templates.TemplateResponse("page2.html", {"request": request})
