// frontend/src/components/CashDisplay.js

import React, {useEffect, useState } from 'react';
import { getCash } from '../api';

export default function CashDisplay({ cash }) {
  return <div>💵 Cash: ${cash}</div>;
}


// export default function CashDisplay() {
//     const [cash, setCash] = useState(0);

//     useEffect(() => {
//         getCash().then((res) => setCash(res.data.cash));
//     }, []);

//     return <div>💵 Cash: ${cash}</div>;
// }

