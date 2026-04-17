from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer
security = HTTPBearer()


async def get_current_user(
        credentials: HTTPBearer = Depends(security)
) -> int:
    """
    ЗАГЛУШКА проверки JWT токена.
    """
    fake_user_id = 1

    return fake_user_id


def create_access_token(user_id: int, telegram_id: int) -> str:
    """
    ЗАГЛУШКА генерации JWT токена.
    Возвращает фейковый токен.
    """
    return "fake-jwt-token-for-testing-12345"