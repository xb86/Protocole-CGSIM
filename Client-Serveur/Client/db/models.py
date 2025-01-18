# /project/db/models.py
from sqlalchemy import Column, Integer, String, Float, DateTime
from db.database import Base  # Import de la base pour les modèles
import datetime

# Modèle Client (Table PostgreSQL)
class Client(Base):
    __tablename__ = "clients"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    credit = Column(Float, default=0)  # Crédits disponibles
    credit_due_date = Column(DateTime, default=datetime.datetime.utcnow)  # Date limite pour régler les crédits

# Modèle Transaction (Table PostgreSQL)
class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, index=True)
    amount = Column(Float)
    date = Column(String)


# Modèle User (Table PostgreSQL)
class User(Base):
    __tablename__ = "users"  # Nom de la table des utilisateurs dans PostgreSQL
    id = Column(Integer, primary_key=True, index=True)  # ID de l'utilisateur
    username = Column(String, unique=True, index=True)  # Nom d'utilisateur unique
    email = Column(String, unique=True, index=True)  # Email unique
    password_hash = Column(String)  # Mot de passe haché pour la sécurité
    created_at = Column(String)  # Date de création du compte
    updated_at = Column(String)  # Date de dernière mise à jour du compte

    def __init__(self, username, email, password_hash, created_at, updated_at):
        self.username = username
        self.email = email
        self.password_hash = password_hash
        self.created_at = created_at
        self.updated_at = updated_at
