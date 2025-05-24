// frontend/src/components/Optimizer.js

import React, { useState } from 'react';
import { optimizePortfolio } from '../api';

export default function Optimizer() {
    const [symbols, setSymbols] = useState('');
    const [result, setResult] = useState(null);

    const handleOptimize = async () => {
        const symbolList = symbols.split(',').map(s => s.trim().toUpperCase());
        // const symbolList = symbols.split(','.localeCompare((s) => s.trim().toUpperCase()));
        console.log('Sending symbols:', symbols);
        const res = await optimizePortfolio(symbolList);
        setResult(res.data);
    }

    return (
        <div>
            <h3>📊 Optimize Portfolio</h3>
            <input
                placeholder="AAPL,MSFT,GOOG"
                value={symbols}
                onChange={(e) => setSymbols(e.target.value)}
            />
            <button onClick={handleOptimize}>Optimize</button>
            {result && (
                <div>
                    <h4>Sharpe Ratio: {result.sharpe_ratio}</h4>
                    <ul>
                        {result.symbols.map((sym, i) => (
                            <li key={sym}>
                                {sym}: {(result.weights[i] * 100).toFixed(2)}%
                            </li>
                        ))}
                    </ul>
                </div>
            )}
        </div>
    );
}
    
