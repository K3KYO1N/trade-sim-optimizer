// frontend/src/components/TradeForm

import React, {useState} from 'react';
import { postTrade } from '../api';

export default function TradeForm({ onTradeSuccess }) {
    const [symbol, setSymbol] = useState('');
    const [action, setAction] = useState('BUY');
    const [quantity, setQuantity] = useState(0);

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            await postTrade({
                symbol,
                action,
                quantity: parseFloat(quantity),
            });
            alert('Trade executed!');
            onTradeSuccess(); //  trigger refresh!
        } catch (err) {
            alert('Trade failed: ' + err.response?.data?.detail || err.message);
        }
    };
    // const handleSubmit = async (e) => {
    //     e.preventDefault();
    //     console.log("Submitting:", { symbol, action, quantity });
    //     await postTrade({ symbol, action, quantity: parseFloat(quantity) });
    //     alert('Trade executed!');
    // };
    
    return(
        <form onSubmit={handleSubmit}>
            <h3>Simulate Trade</h3>
            <input placeholder="Symbol" value={symbol} onChange={(e) => setSymbol(e.target.value.toUpperCase())} />
            <select value={action} onChange={(e) => setAction(e.target.value)}>
                <option value="BUY">BUY</option>
                <option value="SELL">SELL</option>
            </select>
            <input type="number" value={quantity} onChange={(e) => setQuantity(e.target.value)} />
            <button type="submit">Submit</button>
        </form>
    );
    
}