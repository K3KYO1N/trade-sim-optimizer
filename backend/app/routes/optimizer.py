# backend/app/routes/optimizer.py

from fastapi import APIRouter, Query, HTTPException
from app.crud_optimizer import fetch_price_data, optimize_portfolio

router = APIRouter()

@router.get("/")
def get_optimized_allocation(symbols: list[str] = Query(..., description="List of stock tickers")):
    try:
        prices = fetch_price_data(symbols)
        result = optimize_portfolio(prices)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))