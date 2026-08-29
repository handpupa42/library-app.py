from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, EmailStr, Field
class Book(BaseModel):
    id: int
    title: str
    author: str
    isbn: Optional[str] = None
    year: Optional[int] = None
    genre: Optional[str] = None
    available_copies: int = 1

    class Config:
        from_attributes = True

class BookDetail(Book):
    is_available: bool = True
    reader_name: Optional[str] = None

class Reader(BaseModel):
    id: int
    full_name: str
    email: EmailStr | str
    phone: Optional[str] = None
    registration_date: str | datetime

    class Config:
        from_attributes = True

class ReaderProfile(Reader):
    activeBooks: List[str] = []
    reading_history: List[Book] = []


class UserBase(BaseModel):
    username: str = Field(..., min_length=3)
    email: EmailStr
    role: str = "librarian"

class UserCreate(UserBase):
    password: str = Field(..., min_length=6)

class UserUpdate(BaseModel):
    username: Optional[str] = Field(None, min_length=3)
    email: Optional[EmailStr] = None
    password: Optional[str] = Field(None, min_length=6)
    role: Optional[str] = None
    is_active: Optional[bool] = None

class UserResponse(UserBase):
    id: int
    is_active: bool
    created_at: datetime
    reader_id: Optional[int] = None

    class Config:
        from_attributes = True


class LoginRequest(BaseModel):
    username: str
    password: str

class PasswordChangeRequest(BaseModel):
    old_password: str
    new_password: str = Field(..., min_length=6)


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class TokenData(BaseModel):
    username: Optional[str] = None
    role: Optional[str] = None
