from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base
from auth_routes import router as auth_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Library API с Авторизацией JWT",
    description="Модуль 7 — ДЗ 9-10",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(auth_router)


@app.get("/")
def root():
    return {"message": "Перейдите на /docs для работы с API"}

