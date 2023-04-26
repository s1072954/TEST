from typing import Union
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("FAKE_VALUE")
app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/A3", response_class=HTMLResponse)
async def multiple_choice(request: Request):
    return templates.TemplateResponse("test.html", {"request": request})

@app.get("/B2", response_class=HTMLResponse)
async def paraphrasing(request: Request):
    return templates.TemplateResponse("test.html", {"request": request})

@app.get("/B3", response_class=HTMLResponse)
async def stock_prediction(request: Request):
    return templates.TemplateResponse("test.html", {"request": request})

@app.get("/B4-1", response_class=HTMLResponse)
async def stock_prediction(request: Request):
    return templates.TemplateResponse("test.html", {"request": request})

@app.get("/B4-2", response_class=HTMLResponse)
async def stock_prediction(request: Request):
    return templates.TemplateResponse("test.html", {"request": request})

@app.get("/B4-3", response_class=HTMLResponse)
async def stock_prediction(request: Request):
    return templates.TemplateResponse("test.html", {"request": request})

@app.get("/D3-1", response_class=HTMLResponse)
async def stock_prediction(request: Request):
    return templates.TemplateResponse("test.html", {"request": request})

@app.get("/D3-2", response_class=HTMLResponse)
async def stock_prediction(request: Request):
    return templates.TemplateResponse("test.html", {"request": request})
