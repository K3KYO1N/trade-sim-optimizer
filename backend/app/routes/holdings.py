# backend/app/routes/holdings.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud, schemas, database

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[schemas.Holding])
def read_holdings(db: Session = Depends(get_db)):
    return crud.get_holdings(db)

@router.post("/", response_model=schemas.Holding)
def upsert_holding(holding: schemas.HoldingCreate, db: Session = Depends(get_db)):
    return crud.update_holding(
        db, holding.symbol, holding.quantity, holding.cost_basis
    )