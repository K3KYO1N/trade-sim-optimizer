# backend/app/crud_optimizer.py

import numpy as np
import yfinance as yf
import pandas as pd
from scipy.optimize import minimize

def fetch_price_data(symbols, period="1y"):
    data = yf.download(symbols, period=period)["Close"]
    return data.dropna()

def calculate_daily_returns(prices: pd.DataFrame):
    return prices.pct_change().dropna()

def sharpe_ratio(weights, mean_returns, cov_matrix):
    portfolio_return = np.dot(weights, mean_returns)
    portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
    return -portfolio_return / portfolio_volatility

def optimize_portfolio(prices: pd.DataFrame):
    returns = calculate_daily_returns(prices)
    mean_returns = returns.mean()
    cov_matrix = returns.cov()
    num_assets = len(mean_returns)



    initial_guess = [1.0 / num_assets] * num_assets
    bounds = [(0.0, 1.0)] * num_assets
    constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})

    result = minimize(
        sharpe_ratio,
        initial_guess,
        args=(mean_returns, cov_matrix),
        method='SLSQP',
        bounds=bounds,
        constraints=constraints
    )

    rounded_weights = [round(w, 2) for w in result.x]
    rounded_sharpe = round(-result.fun, 2)

    return {
    "weights": rounded_weights,
    "symbols": prices.columns.tolist(),
    "sharpe_ratio": rounded_sharpe
    }

