from fastapi import APIRouter, Depends
from app.schemas import UserProfile, UserGoals, UserRestrictions
from app.security import get_current_user

router = APIRouter(
    prefix="/profile",
    tags=["profile"]
)


@router.get("/", response_model=UserProfile)
async def get_profile(user_id: int = Depends(get_current_user)):
    """
    ЗАГЛУШКА: Получение профиля пользователя.
    Возвращаем объект UserProfile.
    """
    return UserProfile(
        height_cm=180,
        birth_date="2000-01-01",
        current_weight_kg=75.5,
        current_body_fat_pct=14.0
    )


@router.put("/profile", response_model=UserProfile)
async def update_profile(
        profile_data: UserProfile,
        user_id: int = Depends(get_current_user)
):
    """
    ЗАГЛУШКА: Обновление физических параметров профиля.
    """

    return UserProfile(
        height_cm=profile_data.height_cm,
        birth_date=profile_data.birth_date,
        current_weight_kg=profile_data.current_weight_kg,
        current_body_fat_pct=profile_data.current_body_fat_pct
    )


@router.put("/goals", response_model=UserGoals)
async def update_goals(
        goals_data: UserGoals,
        user_id: int = Depends(get_current_user)
):
    """
    ЗАГЛУШКА: Обновление целей пользователя.
    """
    return UserGoals(
        goals_text=goals_data.goals_text
    )


@router.put("/restrictions", response_model=UserRestrictions)
async def update_restrictions(
        restrictions_data: UserRestrictions,
        user_id: int = Depends(get_current_user)
):
    """
    ЗАГЛУШКА: Обновление аллергенов и ограничений.
    """
    return UserRestrictions(
        allergens_text=restrictions_data.allergens_text,
        restrictions_text=restrictions_data.restrictions_text
    )
