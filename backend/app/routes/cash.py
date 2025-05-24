# backend/app/routes/cash.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.crud import calculate_cash_balance

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_cash(db: Session = Depends(get_db)):
    return {"cash": calculate_cash_balance(db)}
