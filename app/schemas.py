from pydantic import BaseModel, Field
from datetime import date
from typing import Optional


class UserRegister(BaseModel):
    """
    Модель для регистрации пользователя.
    """
    telegram_id: int = Field(..., description="Telegram ID пользователя")
    first_name: Optional[str] = Field(None, description="Имя пользователя из Telegram")
    username: Optional[str] = Field(None, description="Username пользователя из Telegram")


class Token(BaseModel):
    """
    Модель ответа с JWT-токеном.
    """
    access_token: str
    token_type: str = "bearer"


class UserProfile(BaseModel):
    """
    Профиль пользователя с физическими параметрами.
    """
    height_cm: Optional[int] = Field(None, description="Рост в сантиметрах")
    birth_date: Optional[date] = Field(None, description="Дата рождения")
    current_weight_kg: Optional[float] = Field(None, description="Текущий вес в кг")
    current_body_fat_pct: Optional[float] = Field(None, description="Процент жира в теле")


class UserGoals(BaseModel):
    """
    Цели пользователя — хранятся свободным текстом.
    """
    goals_text: str = Field(..., description="Свободный текст целей пользователя")


class UserRestrictions(BaseModel):
    """
    Аллергены и ограничения — тоже свободным текстом.
    """
    allergens_text: Optional[str] = Field(None, description="Свободный текст аллергенов")
    restrictions_text: Optional[str] = Field(None, description="Свободный текст ограничений")


class TrainingParseRequestToAI(BaseModel):
    """
    Модель, которую Bot отправляет в AI Service для парсинга тренировки.
    """
    raw_text: str = Field(..., description="Свободный текст всей тренировки")



class FoodCreateToStats(BaseModel):
    """
    Модель, которую Bot отправляет в Statistics Service для добавления питания.
    """
    raw_text: str = Field(..., description="Полный текст питания от пользователя (через запятую)")

