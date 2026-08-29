from pydantic import BaseModel, EmailStr
from typing import List, Optional
class Book(BaseModel):
    id: str
    title: str
    author: str
    year: int
    genre: str

class BookDetail(Book):
    is_available: bool = True
    reader_name: Optional[str] = None

class Reader(BaseModel):
    id: str
    fullName: str
    email: str  
    phone: str
    registrationDate: str

class ReaderProfile(Reader):
    activeBooks: List[str] = []
    reading_history: List[Book] = []
