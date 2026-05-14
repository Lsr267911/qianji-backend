import os

class Settings:
    APP_NAME: str = "千机后端"
    VERSION: str = "1.0.0"
    API_PREFIX: str = "/api/v1"
    CORS_ORIGINS: list = ["*"]
    
    # Questionnaire
    TOTAL_QUESTIONS: int = 160

settings = Settings()
