# backend/app/routes/simulate.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session 
from app.database import SessionLocal
from app import crud, schemas

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/simulate", response_model=schemas.Trade)
def simulate_trade(trade: schemas.TradeCreate, db: Session = Depends(get_db)):
    try:
        return crud.execute_trade(db, trade)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))