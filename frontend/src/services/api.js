import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000/api', 
  headers: { 'Content-Type': 'application/json' }
});

export const suggestHTS = async (description, country) => {
  const response = await api.post('/hts/suggest', { description, country_of_origin: country });
  return response.data;
};

export const processShipment = async (shipment) => {
  const response = await api.post('/workflow/process-shipment', shipment);
  return response.data;
};

export default api;
