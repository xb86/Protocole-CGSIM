# /project/app/api/models.py

from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    user_id: int
    name: str
    email: str
    balance: float
    created_at: str

class Transaction(BaseModel):
    transaction_id: int
    user_id: int
    amount: float
    timestamp: str
    status: str  # 'pending', 'completed', 'failed'

class CreditInfo(BaseModel):
    user_id: int
    credit_amount: float
    credit_expiration: str  # Date d'expiration du crédit
