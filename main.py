from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from schemas import Book, BookDetail, Reader, ReaderProfile
app = FastAPI(
    title="Library API",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
BOOKS_DATA = [
    {
        "id": "1",
        "title": "Мастер и Маргарита",
        "author": "Михаил Булгаков",
        "year": 1967,
        "genre": "Роман",
        "is_available": False,
        "reader_name": "Иван Петров"
    },
    {
        "id": "2",
        "title": "Война и мир",
        "author": "Лев Толстой",
        "year": 1869,
        "genre": "Эпопея",
        "is_available": True,
        "reader_name": None
    },
    {
        "id": "3",
        "title": "Преступление и наказание",
        "author": "Фёдор Достоевский",
        "year": 1866,
        "genre": "Роман",
        "is_available": True,
        "reader_name": None
    }
]
READERS_DATA = [
    {
        "id": "r1",
        "fullName": "Иван Петров",
        "email": "ivan@mail.ru",
        "phone": "+7-999-123-45-67",
        "registrationDate": "2024-01-15",
        "activeBooks": ["1"],
        "reading_history": [
            {
                "id": "2",
                "title": "Война и мир",
                "author": "Лев Толстой",
                "year": 1869,
                "genre": "Эпопея"
            },
            {
                "id": "1",
                "title": "Мастер и Маргарита",
                "author": "Михаил Булгаков",
                "year": 1967,
                "genre": "Роман"
            }
        ]
    },
    {
        "id": "r2",
        "fullName": "Мария Иванова",
        "email": "maria@mail.ru",
        "phone": "+7-999-234-56-78",
        "registrationDate": "2024-02-20",
        "activeBooks": [],
        "reading_history": []
    }
]

@app.get("/", tags=["Главная"])
def root():
    return {"/docs"}

@app.get("/books", response_model=List[Book], tags=["Книги"])
def get_books():
    return BOOKS_DATA

@app.get("/books/{books_id}", response_model=BookDetail, tags=["Книги"])
def get_book_detail(books_id: str):
    for book in BOOKS_DATA:
        if book["id"] == books_id:
            return book
    raise HTTPException(status_code=404, detail="Книга не найдена")

@app.get("/readers", response_model=List[Reader], tags=["Читатели"])
def get_readers():
    return READERS_DATA

@app.get("/readers/{reader_id}", response_model=ReaderProfile, tags=["Читатели"])
def get_reader_profile(reader_id: str):
    for reader in READERS_DATA:
        if reader["id"] == reader_id:
            return reader
    raise HTTPException(status_code=404, detail="Читатель не найден")
