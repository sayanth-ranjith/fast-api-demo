#This is a simple end point url for a fast-api app.
import this

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Book:
    id: int
    title: str
    author: str
    book_name: str
    book_release_date: str

    def __init__(self, id, title, author, book_name, book_release_date):
        self.id = id
        self.title = title
        self.author = author
        self.book_name = book_name
        self.book_release_date = book_release_date

class BookRequest(BaseModel):
    id: int
    title: str
    author: str
    book_name: str
    book_release_date: str

@app.get("/home")
def home() -> dict:
    return {"greeting":"Hello World!"}

@app.get("/ping/{dynamic_number}")
def ping(dynamic_number: str) -> dict:
    dynamic_message = "PONG!" + dynamic_number
    return {"pong": dynamic_message}


@app.post("/books")
def postbook(book_request: BookRequest):
    book = Book(**book_request.model_dump())
    print(book.__dict__)
    print("books posted")
    return {"books": book.author}