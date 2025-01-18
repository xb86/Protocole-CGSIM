from fastapi import APIRouter, HTTPException
from app.api.services import get_user_data, create_new_user
from app.api.services import add_transaction
from app.api.models import Transaction

router = APIRouter()

@router.get("/users/{user_id}")
def get_user(user_id: int):
    return get_user_data(user_id)

@router.post("/users/")
def create_user(user_data: dict):
    return create_new_user(user_data)

@router.post("/transactions/")
async def create_transaction(transaction_data: dict):
    new_transaction = add_transaction(transaction_data)
    if new_transaction:
        return {"message": "Transaction added successfully", "transaction": new_transaction}
    else:
        raise HTTPException(status_code=400, detail="Failed to add transaction")