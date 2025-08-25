import React, { useState } from 'react';
import { processShipment } from '../api';

export default function WorkflowForm() {
  const [shipmentId, setShipmentId] = useState('');
  const [description, setDescription] = useState('');
  const [result, setResult] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const shipment = {
      shipment_id: shipmentId,
      description,
      exporter_name: 'ACME Corp',
      importer_name: 'Maple Inc',
      producer_name: 'ACME Factory',
      hs_code: '010121',
      country_of_origin: 'USA',
      certifier_name: 'John Doe',
      certifier_signature: 'JD',
      certifier_date: '2025-08-25',
      documents: []
    };
    const data = await processShipment(shipment);
    setResult(data);
  };

  return (
    <div style={{ marginTop: '20px' }}>
      <h2>Process Shipment</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={shipmentId}
          onChange={(e) => setShipmentId(e.target.value)}
          placeholder="Shipment ID"
          required
        />
        <input
          type="text"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          placeholder="Item description"
          required
        />
        <button type="submit">Process</button>
      </form>
      {result && (
        <div>
          <p>Shipment ID: {result.shipment_id}</p>
          <p>Status: {result.status}</p>
          <p>Message: {result.message}</p>
        </div>
      )}
    </div>
  );
}
