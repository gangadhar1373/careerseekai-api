from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import config as settings

DATABASE_URL = settings.settings.DATABASE_URL
# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL, echo=True)
# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Create a base class for declarative models
Base = declarative_base()
# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()