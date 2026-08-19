from fastapi import FastAPI, HTTPException
app = FastAPI(
    title="Library API",
    description="API",
    version="1.0.0"
)

books = [
    {
        "id": "1",
        "title": "Мастер и Маргарита",
        "author": "Михаил Булгаков",
        "year": 1967,
        "genre": "Роман",
        "isAvailable": False,
        "description": "Мистический роман о дьяволе, посетившем Москву в 1930-х годах."
    },
    {
        "id": "2",
        "title": "Война и мир",
        "author": "Лев Толстой",
        "year": 1869,
        "genre": "Эпопея",
        "isAvailable": True,
        "description": "Масштабное произведение о русском обществе в эпоху наполеоновских войн."
    },
    {
        "id": "3",
        "title": "Преступление и наказание",
        "author": "Фёдор Достоевский",
        "year": 1866,
        "genre": "Роман",
        "isAvailable": True,
        "description": "Психологический роман о студенте Раскольникове и его теории."
    },
    {
        "id": "4",
        "title": "Евгений Онегин",
        "author": "Александр Пушкин",
        "year": 1833,
        "genre": "Роман в стихах",
        "isAvailable": False,
        "description": "История о разочарованном дворянине и трагической любви."
    }
]

readers = [
    {
        "id": "r1",
        "fullName": "Иван Петров",
        "email": "ivan@mail.ru",
        "phone": "+7-999-123-45-67",
        "registrationDate": "2024-01-15",
        "activeBooks": ["1"],
        "booksHistory": [
            {
                "bookId": "2",
                "title": "Война и мир",
                "takenAt": "2024-02-01",
                "returnedAt": "2024-03-15"
            },
            {
                "bookId": "1",
                "title": "Мастер и Маргарита",
                "takenAt": "2024-08-15",
                "returnedAt": None
            }
        ]
    },
    {
        "id": "r2",
        "fullName": "Мария Иванова",
        "email": "maria@mail.ru",
        "phone": "+7-999-234-56-78",
        "registrationDate": "2024-02-20",
        "activeBooks": ["2"],
        "booksHistory": [
            {
                "bookId": "2",
                "title": "Война и мир",
                "takenAt": "2024-05-10",
                "returnedAt": None
            }
        ]
    }
]


@app.get("/books", tags=["книги"])
def get_all_books():
    return books


@app.get("/books/{books_id}", tags=["книги"])
def get_book_by_id(books_id: str):
    for book in books:
        if book["id"] == books_id:
            return book
    raise HTTPException(status_code=404, detail="книга не найдена")

@app.get("/readers", tags=["читатели"])
def get_all_readers():
    return readers

@app.get("/readers/{reader_id}", tags=["читатели"])
def get_reader_by_id(reader_id: str):
    for reader in readers:
        if reader["id"] == reader_id:
            return reader
    raise HTTPException(status_code=404, detail="читатель не найден")