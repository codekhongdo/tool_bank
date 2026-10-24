from pydantic_settings import BaseSettings,SettingsConfigDict
from functools import lru_cache
class Settings(BaseSettings):
    SEPAY_API_TOKEN: str
    SEPAY_WEBHOOK_AUTH_TOKEN: str
    BANK_ACCOUNT_NUMBER: str = ""
    EXPECTED_CODE: str = "THCSC3"
    EXCEL_OUTPUT_DIR: str = "data/exports"
    EXCEL_FILE_NAME: str = "payments.xlsx"
    APP_HOST: str = "127.0.0.1"
    APP_PORT: int = 8000
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )
@lru_cache()
def get_settings() ->Settings:
    return Settings()
 