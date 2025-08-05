# app/config.py
import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env

class Settings:
    DATABASE_URL: str = os.getenv("DATABASE_URL") or ""

    def __init__(self):
        if not self.DATABASE_URL:
            raise ValueError("DATABASE_URL environment variable is not set")

settings = Settings()