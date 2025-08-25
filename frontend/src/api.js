import axios from 'axios';

const api = axios.create({
  baseURL: '/api',  // proxy на FastAPI
  headers: { 'Content-Type': 'application/json' },
});

export const getHTSCode = async (description) => {
  const response = await api.post('/hts/suggest', { description });
  return response.data;
};

export const checkUSMCA = async (description) => {
  const response = await api.post('/usmca/check', { description });
  return response.data;
};

export const processShipment = async (shipment) => {
  const response = await api.post('/workflow/process-shipment', shipment);
  return response.data;
};

export default api;
