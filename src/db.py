"""
db.py Настройка подключения к базе данных.
"""

import uuid
from sqlalchemy import Column, String, Text, DateTime, create_engine
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.sql import func
from pgvector.sqlalchemy import Vector

from pydantic import BaseModel

DATABASE_URL = (
    "postgresql+psycopg2://lab_user:strong_password@localhost:5432/lab_checker"
)

engine = create_engine(
    DATABASE_URL,
    echo=True,  # логирование SQL
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

Base = declarative_base()


class Lab(BaseModel):
    __tablename__ = "labs"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    last_name = Column(String, nullable=False)
    group_name = Column(String, nullable=False)

    bash_code = Column(Text, nullable=False)
    code_vector = Column(Vector(384))  # embedding размером 384

    execution_result = Column(Text)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
