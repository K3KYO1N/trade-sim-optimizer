# backend/app/routes/snapshots.py

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

@router.post("/", response_model=schemas.Snapshot)
def create_snapshot(shanpshot: schemas.SnapshotCreate, db: Session = Depends(get_db)):
    return crud.create_snapshot(db, snapshot)

@router.get("/", response_model=list[schemas.Snapshot])
def read_snapshots(skip:int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_snapshots(db, skip, limit)

@router.delete("/{snapshot_id}", response_model=schemas.Snapshot)
def delete_snapshot(snapshot_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_snapshot(db, snapshot_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Snapshot not found")
    return deleted