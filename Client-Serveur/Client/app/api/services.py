# /project/app/api/services.py

from db.crud import get_user_from_db, add_user_to_db, add_transaction_to_db
from app.api.models import User, Transaction

# Récupérer les données d'un utilisateur
def get_user_data(user_id: int) -> User:
    user_data = get_user_from_db(user_id)
    if user_data:
        return User(**user_data)  # Utilisation de Pydantic pour la validation et la conversion en modèle
    else:
        return None  # L'utilisateur n'existe pas

# Ajouter un nouvel utilisateur
def create_new_user(user_data: dict) -> User:
    new_user = add_user_to_db(user_data)
    if new_user:
        return User(**new_user)
    else:
        return None

# Ajouter une transaction
def add_transaction(transaction_data: dict) -> Transaction:
    # Exemple d'ajout de transaction
    new_transaction = add_transaction_to_db(transaction_data)
    if new_transaction:
        return Transaction(**new_transaction)
    else:
        return None

def use_credit_for_purchase(client_id, amount):
    client = get_user_from_db(client_id)
    if client and client.credit >= amount:
        # Soustraire le montant du crédit
        client.credit -= amount
        # Créer une transaction avec un crédit utilisé
        new_transaction = Transaction(client_id=client_id, amount=-amount, date=str(datetime.datetime.now()))
        add_transaction_to_db(new_transaction)
        return {"status": "success", "message": "Transaction processed with credit"}
    else:
        return {"status": "failed", "message": "Insufficient credit"}

