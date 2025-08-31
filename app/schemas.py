from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List
from datetime import datetime

class TransactionBase(BaseModel):
    amount: float = Field(..., description="Positive for credit, negative for debit")
    description: Optional[str] = None

class TransactionCreate(TransactionBase):
    pass

class TransactionOut(TransactionBase):
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    name: str
    email: EmailStr
    phone: str

class UserCreate(UserBase):
    pass

class UserOut(UserBase):
    id: int
    wallet_balance: float

    class Config:
        orm_mode = True

class UserDetail(UserOut):
    transactions: List[TransactionOut] = []