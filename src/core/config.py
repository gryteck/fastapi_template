import logger
import pathlib

from dotenv import dotenv_values
from pydantic import Field
from pydantic_settings import BaseSettings

env_path = pathlib.Path(__file__).cwd().parent.parent / '.env'
env_values = dotenv_values(env_path)

if not env_values:
    print(f"Warning: No environment variables loaded from {env_path}")


class Settings(BaseSettings):
    app_name: str = Field('API кинотеатра', alias='APP_NAME')


settings = Settings()
