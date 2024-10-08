from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    MODE: Literal['DEV', 'TEST', 'PROD']
    LOG_LEVEL: Literal['DEBUG', 'INFO']

    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    # @root_validator(skip_on_failure=True)
    # def get_database_url(cls, values):
    #     values['DATABASE_URL'] = (
    #         f"postgresql+asyncpg://{values['DB_USER']}:{values['DB_PASS']}@"
    #         f"{values['DB_HOST']}:{values['DB_PORT']}/{values['DB_NAME']}"
    #     )
    #     return values

    @property
    def DATABASE_URL(self):
        return (
            f'postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@'
            f'{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'
        )

    TEST_DB_HOST: str
    TEST_DB_PORT: int
    TEST_DB_USER: str
    TEST_DB_PASS: str
    TEST_DB_NAME: str

    @property
    def TEST_DATABASE_URL(self):
        return (
            f'postgresql+asyncpg://{self.TEST_DB_USER}:{self.TEST_DB_PASS}@'
            f'{self.TEST_DB_HOST}:{self.TEST_DB_PORT}/{self.TEST_DB_NAME}'
        )

    SECRET_KEY: str
    ALGORITHM: str

    SMTP_HOST: str
    SMTP_PORT: int
    SMTP_USER: str
    SMTP_PASS: str

    REDIS_HOST: str
    REDIS_PORT: int
    SENTRY_DSN: str

    model_config = SettingsConfigDict(env_file='.env')


settings = Settings()
