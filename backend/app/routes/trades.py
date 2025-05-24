 # backend/app/routes/trades.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud, schemas, database

router = APIRouter()

# Dependency: Get DB session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.Trade)
def create_trade(trade: schemas.TradeCreate, db: Session = Depends(get_db)):
    return crud.create_trade(db, trade)

@router.get("/", response_model=list[schemas.Trade])
def read_trades(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_trades(db, skip, limit)
