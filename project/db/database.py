import psycopg2
from config.settings import DATABASE_URL
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Connection à PostgreSQL
SQLALCHEMY_DATABASE_URL = "postgresql://user:password@localhost/mydatabase"  # Change les valeurs

# Configuration du moteur SQLAlchemy
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})  # Spécifique à SQLite, pas nécessaire pour PostgreSQL

# Configuration de la session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base pour les modèles
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_connection():
    conn = psycopg2.connect(DATABASE_URL)
    return conn
