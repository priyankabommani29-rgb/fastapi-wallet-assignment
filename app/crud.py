from sqlalchemy.orm import Session
from sqlalchemy import func
from . import models, schemas

# Users

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(name=user.name, email=user.email, phone=user.phone)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_users_with_balance(db: Session):
    # returns list of tuples (User, balance)
    subq = db.query(models.Transaction.user_id, func.coalesce(func.sum(models.Transaction.amount), 0).label("balance")).group_by(models.Transaction.user_id).subquery()
    q = db.query(models.User, func.coalesce(subq.c.balance, 0)).outerjoin(subq, models.User.id == subq.c.user_id)
    return q.all()


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

# Transactions

def create_transaction(db: Session, user_id: int, tx: schemas.TransactionCreate):
    db_tx = models.Transaction(user_id=user_id, amount=tx.amount, description=tx.description)
    db.add(db_tx)
    db.commit()
    db.refresh(db_tx)
    return db_tx


def get_transactions_for_user(db: Session, user_id: int):
    return db.query(models.Transaction).filter(models.Transaction.user_id == user_id).order_by(models.Transaction.timestamp.desc()).all()


def get_balance_for_user(db: Session, user_id: int):
    res = db.query(func.coalesce(func.sum(models.Transaction.amount), 0)).filter(models.Transaction.user_id == user_id).scalar()
    return float(res or 0)