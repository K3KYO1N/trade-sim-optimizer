// frontend/src/components/HoldingsList.js

import React, {useEffect, useState} from 'react';
import { getHoldings } from '../api';

export default function HoldingsList({ holdings }) {
  return (
    <div>
      <h3>📦 Holdings</h3>
      <ul>
        {holdings.map((h) => (
          <li key={h.id}>{h.symbol} - {h.quantity} @ ${h.cost_basis.toFixed(2)}</li>
        ))}
      </ul>
    </div>
  );
}


// export default function HoldingsList(){
//     const [holdings, setHoldings] = useState([]);

//     useEffect(() => {
//         getHoldings().then((res) => setHoldings(res.data));
//     }, []);

//     return(
//         <div>
//             <h3>📦 Holdings</h3>
//             <ul>
//                 {holdings.map((h) => (
//                     <li key={h.id}>
//                         {h.symbol} - {h.quantity} @ ${h.cost_basis.toFixed(2)}
//                     </li>
//                 ))}
//             </ul>
//         </div>
//     );
// }