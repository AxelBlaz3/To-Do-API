from pydantic import BaseSettings


class Settings(BaseSettings):
    """Settings class that loads env vars upon startup."""
    mongodb_uri: str
    mongo_db: str = 'todo'

    class Config:
        env_file = '.env'
