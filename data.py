from datetime import date
BOOKS_DATA = [
    {
        "title": "Мастер и Маргарита",
        "author": "Михаил Булгаков",
        "isbn": "978-5-389-01686-6",
        "year": 1967,
        "genre": "Роман",
        "available_copies": 2
    },
    {
        "title": "Война и мир",
        "author": "Лев Толстой",
        "isbn": "978-5-17-090335-2",
        "year": 1869,
        "genre": "Эпопея",
        "available_copies": 3
    },
    {
        "title": "Преступление и наказание",
        "author": "Фёдор Достоевский",
        "isbn": "978-5-389-02281-2",
        "year": 1866,
        "genre": "Роман",
        "available_copies": 1
    },
    {
        "title": "Евгений Онегин",
        "author": "Александр Пушкин",
        "isbn": "978-5-17-080000-1",
        "year": 1833,
        "genre": "Роман в стихах",
        "available_copies": 4
    },
    {
        "title": "1984",
        "author": "Джордж Оруэлл",
        "isbn": "978-5-4467-0012-3",
        "year": 1949,
        "genre": "Антиутопия",
        "available_copies": 2
    },
    {
        "title": "Маленький принц",
        "author": "Антуан де Сент-Экзюпери",
        "isbn": "978-5-9287-2510-4",
        "year": 1943,
        "genre": "Сказка",
        "available_copies": 5
    },
    {
        "title": "Анна Каренина",
        "author": "Лев Толстой",
        "isbn": "978-5-389-01234-5",
        "year": 1877,
        "genre": "Роман",
        "available_copies": 1
    }
]
READERS_DATA = [
    {
        "full_name": "Иван Петров",
        "email": "ivan@mail.ru",
        "phone": "+7-999-123-45-67",
        "registration_date": date(2024, 1, 15)
    },
    {
        "full_name": "Мария Иванова",
        "email": "maria@mail.ru",
        "phone": "+7-999-234-56-78",
        "registration_date": date(2024, 2, 20)
    },
    {
        "full_name": "Пётр Сидоров",
        "email": "petr@mail.ru",
        "phone": "+7-999-345-67-89",
        "registration_date": date(2024, 3, 10)
    },
    {
        "full_name": "Елена Смирнова",
        "email": "elena@mail.ru",
        "phone": "+7-999-456-78-90",
        "registration_date": date(2024, 4, 5)
    },
    {
        "full_name": "Алексей Новиков",
        "email": "alexey@mail.ru",
        "phone": "+7-999-567-89-01",
        "registration_date": date(2024, 5, 12)
    }
]

HISTORY_DATA = [
    (1, 1, date(2024, 2, 1), date(2024, 2, 20)),
    (1, 2, date(2024, 3, 1), date(2024, 3, 15)),
    (1, 3, date(2024, 4, 1), None), 

    (2, 4, date(2024, 2, 25), date(2024, 3, 10)),
    (2, 5, date(2024, 3, 12), date(2024, 3, 28)),
    (2, 6, date(2024, 4, 5), None),  

    (3, 1, date(2024, 3, 15), date(2024, 4, 1)),
    (3, 7, date(2024, 4, 2), date(2024, 4, 18)),
    (3, 2, date(2024, 4, 20), None), 

    (4, 3, date(2024, 4, 10), date(2024, 4, 25)),
    (4, 4, date(2024, 4, 26), date(2024, 5, 10)),
    (4, 5, date(2024, 5, 12), None),  
    (5, 6, date(2024, 5, 15), date(2024, 5, 30)),
    (5, 7, date(2024, 6, 1), None),   
    (5, 1, date(2024, 6, 5), None)    
]
USERS_DATA = [
    {
        "username": "admin",
        "email": "admin@library.ru",
        "password": "admin123",
        "role": "admin"
    },
    {
        "username": "librarian1",
        "email": "lib1@library.ru",
        "password": "lib12345",
        "role": "librarian"
    },
    {
        "username": "librarian2",
        "email": "lib2@library.ru",
        "password": "lib67890",
        "role": "librarian"
    }
]
