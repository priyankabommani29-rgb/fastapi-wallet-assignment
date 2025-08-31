from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from . import crud, schemas, models
from .deps import get_db

router = APIRouter()

@router.post("/users", response_model=schemas.UserOut)
def create_user(user_in: schemas.UserCreate, db: Session = Depends(get_db)):
    # basic duplicate email/phone checks
    exists_email = db.query(models.User).filter(models.User.email == user_in.email).first()
    if exists_email:
        raise HTTPException(status_code=400, detail="Email already registered")
    exists_phone = db.query(models.User).filter(models.User.phone == user_in.phone).first()
    if exists_phone:
        raise HTTPException(status_code=400, detail="Phone already registered")
    user = crud.create_user(db, user_in)
    return {"id": user.id, "name": user.name, "email": user.email, "phone": user.phone, "wallet_balance": 0.0}

@router.get("/users", response_model=List[schemas.UserOut])
def list_users(db: Session = Depends(get_db)):
    rows = crud.get_users_with_balance(db)
    result = []
    for user, balance in rows:
        result.append({"id": user.id, "name": user.name, "email": user.email, "phone": user.phone, "wallet_balance": float(balance or 0)})
    return result

@router.post("/users/{user_id}/wallet", response_model=schemas.TransactionOut)
def update_wallet(user_id: int, tx_in: schemas.TransactionCreate, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    # create transaction
    tx = crud.create_transaction(db, user_id, tx_in)
    return tx

@router.get("/users/{user_id}/transactions", response_model=List[schemas.TransactionOut])
def fetch_transactions(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    txs = crud.get_transactions_for_user(db, user_id)
    return txs