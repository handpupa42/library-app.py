from database import engine, SessionLocal, Base
from models import Book, Reader, reader_books
from data import BOOKS_DATA, READERS_DATA, HISTORY_DATA


def seed_database():
    print("Создание таблиц и очистка данных...")
    Base.metadata.create_all(bind=engine)
    
    db = SessionLocal()
    
    try:
        db.execute(reader_books.delete())
        db.query(Reader).delete()
        db.query(Book).delete()
        db.commit()
        print("База данных очищена")

        books = [Book(**book_data) for book_data in BOOKS_DATA]
        db.add_all(books)
        db.commit()
        print(f"Добавлено книг: {len(books)}")
        readers = [Reader(**reader_data) for reader_data in READERS_DATA]
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
        print(f"Добавлено записей в историю: {len(HISTORY_DATA)}")
        print("Наполнение базы данных успешно завершено!")

    except Exception as e:
        db.rollback()
        print(f"Ошибка при заполнении базы данных: {e}")
    finally:
        db.close()


if __name__ == "__main__":
    seed_database()
