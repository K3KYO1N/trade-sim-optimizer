// frontend/src/App.js
// import React from 'react';
import React, { useState, useEffect } from 'react';
import TradeForm from './components/TradeForm';
import HoldingsList from './components/HoldingsList';
import CashDisplay from './components/CashDisplay';
import Optimizer from './components/Optimizer';
import { getHoldings, getCash } from './api';

function App() {
  const [holdings, setHoldings] = useState([]);
  const [cash, setCash] = useState(0);

  const refreshData = async () => {
    const holdingsRes = await getHoldings();
    const cashRes = await getCash();
    setHoldings(holdingsRes.data);
    setCash(cashRes.data.cash);
  };

  useEffect(() => {
    refreshData();
  }, []);

  return (
    <div className="App" style={{ padding: '2rem' }}>
      <h1>💹 Trade Simulator & Portfolio Optimizer</h1>
      <CashDisplay cash={cash} />
      <HoldingsList holdings={holdings} />
      <TradeForm onTradeSuccess={refreshData} />
      <Optimizer />
    </div>
  )
}
 export default App;




//  // frontend/src/App.js
// import React from 'react';
// import TradeForm from './components/TradeForm';
// import HoldingsList from './components/HoldingsList';
// import CashDisplay from './components/CashDisplay';
// import Optimizer from './components/Optimizer';

// function App() {
//   return (
//     <div className="App" style={{ padding: '2rem' }}>
//       <h1>💹 Trade Simulator & Portfolio Optimizer</h1>
//       <CashDisplay />
//       <HoldingsList />
//       <TradeForm />
//       <Optimizer />
//     </div>
//   )
// }
//  export default App;