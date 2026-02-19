"""
main.py
Точка входа в приложение.
Создает FastAPI приложение и подключает роуты.
"""

from fastapi import FastAPI
from api.routes import router

app = FastAPI(title="Lab Checker Service")

app.include_router(router)
