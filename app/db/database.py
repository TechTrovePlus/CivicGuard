import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# dotenv acts as the loader (reads->key-value pairs->inside .env-> and injects them into the running system's environment)
# os acts as the fetcher (os can -> retrieve those newly injected variables)
# SQLAlchemy = High-level ORM(Object-Relational Mapping) and database toolkit that manages sessions, queries, and connection pooling.
# psycopg = Low-level PostgreSQL driver used by SQLAlchemy.

# Load values from .env into environment variables
load_dotenv()

# Read environment variables
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
database = os.getenv("DB_NAME")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")

# Build PostgreSQL connection URL
DATABASE_URL = (
    f"postgresql+psycopg://{user}:{password}@{host}:{port}/{database}"
)

#engine (database-connection  manager) provides connection
# This acts as the central connection pool to your PostgreSQL database
engine = create_engine(DATABASE_URL)

#SessionLocal (factory to create session)
# This will generate new database sessions for your FastAPI endpoints
SessionLocal = sessionmaker(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

