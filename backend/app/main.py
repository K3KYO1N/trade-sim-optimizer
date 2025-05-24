 # backend/app/main.py
from fastapi import FastAPI
from app.routes import trades, holdings, snapshots, simulate, cash, optimizer
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Trade Simulation API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(trades.router, prefix="/trades")
app.include_router(holdings.router, prefix="/holdings")
app.include_router(snapshots.router, prefix="/snapshots")
app.include_router(simulate.router, prefix="/trade")
app.include_router(cash.router, prefix="/cash")
app.include_router(optimizer.router, prefix="/optimizer")

