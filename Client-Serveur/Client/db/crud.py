# /project/db/crud.py
from sqlalchemy.orm import Session
from db.database import get_db  # Pour obtenir une session DB
from app.api.models import User, Transaction  # Import des modèles User et Transaction

# Fonction pour récupérer un utilisateur depuis la base de données
def get_user_from_db(user_id: int, db: Session):
    user = db.query(User).filter(User.id == user_id).first()  # Recherche de l'utilisateur par ID
    return user  # Renvoie l'utilisateur si trouvé, sinon None

# Fonction pour ajouter un utilisateur dans la base de données
def add_user_to_db(user_data: dict, db: Session):
    # Création d'un objet User avec les données fournies
    new_user = User(
        username=user_data["username"],
        email=user_data["email"],
        password_hash=user_data["password_hash"],  # Assurez-vous que le mot de passe est haché avant de l'envoyer
        created_at=user_data["created_at"],
        updated_at=user_data["updated_at"]
    )
    db.add(new_user)  # Ajoute le nouvel utilisateur à la session
    db.commit()  # Effectue la transaction et enregistre dans la base
    db.refresh(new_user)  # Récupère l'utilisateur après l'ajout pour obtenir l'ID généré
    return new_user  # Retourne l'utilisateur ajouté

# Fonction pour ajouter une transaction dans la base de données
def add_transaction_to_db(transaction_data: dict):
    db = next(get_db())
    new_transaction = Transaction(**transaction_data)
    db.add(new_transaction)
    db.commit()
    return new_transaction