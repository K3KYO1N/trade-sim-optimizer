import axios from 'axios';
import qs from 'qs';

const BASE_URL = 'http://localhost:8000';

export const getHoldings = () => axios.get(`${BASE_URL}/holdings`);
export const getCash = () => axios.get(`${BASE_URL}/cash`);
export const getTrades = () => axios.get(`${BASE_URL}/trades`);
export const postTrade = (data) => axios.post(`${BASE_URL}/trade/simulate`, data);
export const optimizePortfolio = (symbols) =>
    axios.get(`${BASE_URL}/optimizer`, { 
        params: { symbols }, 
        paramsSerializer: (params) => qs.stringify(params, { arrayFormat: 'repeat' })
    });