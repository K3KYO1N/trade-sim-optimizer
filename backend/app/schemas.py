# backend/app/schemas.py
from pydantic import BaseModel
from datetime import datetime

# Trades ==========================
class TradeBase(BaseModel):
    symbol: str
    action: str
    quantity: float
    price: float

class TradeCreate(BaseModel):
    symbol: str
    action: str
    quantity: float

class Trade(TradeBase):
    id: int 
    timestamp: datetime

    class Config:
        orm_mode = True

# Holdings ========================
class HoldingBase(BaseModel):
    symbol: str
    quantity: float
    cost_basis: float

class HoldingCreate(HoldingBase):
    pass

class Holding(HoldingBase):
    id: int

    class Config:
        orm_mode = True

# Snapshots =======================================
class SnapshotBase(BaseModel):
    cash: float
    total_value: float

class SnapshotCreate(SnapshotBase):
    pass

class Snapshot(SnapshotBase):
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True