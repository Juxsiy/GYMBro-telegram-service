from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers.auth import router as auth_router
from app.routers.profile import router as profile_router

app = FastAPI(
    title="Bot + User Service",
    description="Сервис пользователей, регистрации и профиля для фитнес-бота",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(profile_router)


@app.get("/")
async def root():
    """
    Проверки, что сервис работает.
    """
    return {
        "message": "Bot + User Service is running",
        "status": "ok",
        "version": "0.1.0",
        "documentation": "/docs"
    }
