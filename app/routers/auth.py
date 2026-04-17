from fastapi import APIRouter
from app.schemas import UserRegister, Token

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

@router.post("/register", response_model=Token)
async def register(user_data: UserRegister):
    """
    ЗАГЛУШКА: Регистрация пользователя по Telegram ID.
    Возвращает фейковый JWT токен.
    """
    return Token(
        access_token="fake-jwt-token-for-testing-12345",
        token_type="bearer"
    )