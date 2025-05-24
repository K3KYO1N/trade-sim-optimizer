# backend/app/crud.py
from sqlalchemy.orm import Session
from app import models, schemas
from app.utils import fetch_current_price
from app.schemas import TradeCreate
from datetime import datetime


# trades =========================================================
def create_trade(db: Session, trade: schemas.TradeCreate):
    db_trade = models.Trade(**trade.dict())
    db.add(db_trade)
    db.commit()
    db.refresh(db_trade)
    return db_trade

def get_trades(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Trade).offset(skip).limit(limit).all()

def execute_trade(db: Session, trade_data: TradeCreate):
    price = fetch_current_price(trade_data.symbol)
    price = float(price)

    print("RAW action:", trade_data.action)
    quantity = trade_data.quantity
    action = trade_data.action.strip().upper()
    cost = quantity * price
    print("Normalized action:", action) 
    
    cash = calculate_cash_balance(db)

    holding = db.query(models.Holding).filter(models.Holding.symbol == trade_data.symbol).first()

    if action == "BUY":
        if cash < cost:
            raise ValueError(f"Not enough cash. You have ${cash}, need ${cost}")
        if holding:
            total_cost = (holding.quantity * holding.cost_basis) + cost
            holding.quantity += quantity
            holding.cost_basis = float(total_cost / holding.quantity)

        else:
            holding = models.Holding(symbol=trade_data.symbol, quantity=quantity, cost_basis=price)
            db.add(holding)

    elif action == "SELL":
        if not holding or holding.quantity < quantity:
            raise ValueError("Not enough shares to sell.")
        holding.quantity -= quantity
        if holding.quantity == 0:
            db.delete(holding)
        
    else:
        raise ValueError("Invalid action. use BUY or SELL.")

    new_trade = models.Trade(
        symbol=trade_data.symbol,
        action=action,
        quantity=quantity,
        price=price
    )
    db.add(new_trade)
    db.commit()
    db.refresh(new_trade)

    return new_trade

# holdings ======================================================
def get_holdings(db: Session):
    return db.query(models.Holding).all()

def update_holding(db: Session, symbol: str, quantity: float, cost_basis: float):
    # quantity = float(quantity)
    # cost_basis = float(cost_basis)

    holding = db.query(models.Holding).filter(models.Holding.symbol == symbol).first()
    if holding:
        holding.quantity = quantity
        holding.cost_basis = cost_basis
    else:
        holding = models.Holding(symbol=symbol, quantity=quantity, cost_basis=cost_basis)
        db.add(holding)
    db.commit()
    db.refresh(holding)
    return holding

# snapshots ====================================================
def create_snapshot(db: Session, snapshot: schemas.SnapshotCreate):
    db_snapshot = models.Snapshot(**Snapshot.dict())
    db.add(db_snapshot)
    db.commit()
    db.refresh(db_snapshot)
    return db_snapshot

def get_snapshots(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Snapshot).offset(skip).limit(limit).all()

def delete_snapshot(db: Session, snapshot_id: int):
    snapshot = db.query(models.Snapshot).filter(models.Snapshot.id == snapshot_id).first()
    if snapshot:
        db.delete(snapshot)
        db.commit()
    return snapshot

# cash ==========================================================
INITIAL_CASH = 10000.0

def calculate_cash_balance(db: Session, initial_cash: float = INITIAL_CASH) -> float:
    trades = db.query(models.Trade).all()
    cash = initial_cash
    for trade in trades:
        cost = trade.quantity * trade.price
        if trade.action.upper() == "BUY":
            cash -= cost
        elif trade.action.upper() == "SELL":
            cash += cost
    return round(cash, 2)    

