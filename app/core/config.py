from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    OPENAI_API_KEY: str
    # URLs to backend microservices
    USER_SERVICE_URL: str = "http://user-service:8000"
    CRM_SERVICE_URL: str = "http://crm-service:8000"
    PRICING_SERVICE_URL: str = "http://pricing-service:8000"

    class Config:
        env_file = ".env"

settings = Settings()