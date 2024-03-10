import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import random
import requests
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.INFO)

app = FastAPI()

class UrlObjectModel(BaseModel):
    url: str


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/send-url/")
async def receive_url(urlObject: UrlObjectModel):

    url = urlObject.url

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        
        print(soup.prettify())
    else:
        print("Failed to retrieve the webpage")
    return {"message": f"Received URL: {url}"}
