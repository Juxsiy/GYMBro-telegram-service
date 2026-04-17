# app/models.py

from sqlalchemy import Column, Integer, String, Float, Date, DateTime, Text, BigInteger, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()


class User(Base):
    """Основная таблица пользователей"""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    telegram_id = Column(BigInteger, unique=True, nullable=False, index=True)
    first_name = Column(String(128), nullable=True)
    username = Column(String(128), nullable=True)

    registered_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class UserProfile(Base):
    """Профиль пользователя"""
    __tablename__ = "user_profiles"

    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)

    height_cm = Column(Integer, nullable=True)
    birth_date = Column(Date, nullable=True)
    current_weight_kg = Column(Float, nullable=True)
    current_body_fat_pct = Column(Float, nullable=True)

    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = relationship("User", backref="profile")


class UserGoals(Base):
    """Цели пользователя — свободный текст"""
    __tablename__ = "user_goals"

    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)

    goals_text = Column(Text, nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = relationship("User", backref="goals")


class UserRestrictions(Base):
    """Аллергены и ограничения — свободный текст"""
    __tablename__ = "user_restrictions"

    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)

    allergens_text = Column(Text, nullable=True)
    restrictions_text = Column(Text, nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = relationship("User", backref="restrictions")