from functools import lru_cache
import app.config
from fastapi.security import OAuth2PasswordBearer


@lru_cache()
def get_settings() -> app.config.Settings:
    """Getter for settings object.

    Returns:
        app.config.Settings: Settings that holds env vars.
    """
    return app.config.Settings()


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
