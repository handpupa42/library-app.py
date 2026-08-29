from database import engine, SessionLocal, Base
from models import Book, Reader, User, reader_books
from data import BOOKS_DATA, READERS_DATA, HISTORY_DATA, USERS_DATA
from auth import get_password_hash
def seed_database():
    print("Пересоздание таблиц и заполнение базой данных...")

    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    try:
        # Очистка таблиц
        db.execute(reader_books.delete())
        db.query(User).delete()
        db.query(Reader).delete()
        db.query(Book).delete()
        db.commit()
        print("Таблицы очищены")

        books = [Book(**b) for b in BOOKS_DATA]
        db.add_all(books)
        db.commit()
        print(f"Добавлено книг: {len(books)}")

        readers = [Reader(**r) for r in READERS_DATA]
        db.add_all(readers)
        db.commit()
        print(f"Добавлено читателей: {len(readers)}")

        for reader_id, book_id, taken_at, returned_at in HISTORY_DATA:
            stmt = reader_books.insert().values(
                reader_id=reader_id,
                book_id=book_id,
                taken_at=taken_at,
                returned_at=returned_at
            )
            db.execute(stmt)
        db.commit()
        print(f" Добавлено записей истории: {len(HISTORY_DATA)}")
        users = []
        for u_data in USERS_DATA:
            raw_password = u_data.pop("password")
            u_data["password_hash"] = get_password_hash(raw_password)
            users.append(User(**u_data))

        db.add_all(users)
        db.commit()
        print(f"Добавлено пользователей: {len(users)}")

        print("Наполнение базы данных успешно завершено!")

    except Exception as e:
        db.rollback()
        print(f"Ошибка при сидинге: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    seed_database()

