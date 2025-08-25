import React, { useState } from 'react';
import { processShipment } from '../services/api';

function UploadPage() {
  const [file, setFile] = useState(null);
  const [results, setResults] = useState([]);

  const handleFileChange = (e) => setFile(e.target.files[0]);

  const handleUpload = () => {
    if (!file) return;

    const reader = new FileReader();
    reader.onload = async (e) => {
      const csvText = e.target.result;
      const rows = csvText.split('\n').map(r => r.split(','));
      const shipments = rows.map(r => ({
        exporter_name: r[0],
        importer_name: r[1],
        producer_name: r[2],
        description: r[3],
        hs_code: r[4],
        country_of_origin: r[5],
        certifier_name: r[6],
        certifier_signature: r[7],
        certifier_date: r[8],
        documents: [], 
        shipment_id: `SHP-${Math.floor(Math.random() * 10000)}`,
      }));

      const processed = [];
      for (const shipment of shipments) {
        const res = await processShipment(shipment);
        processed.push(res);
      }
      setResults(processed);
    };
    reader.readAsText(file);
  };

  return (
    <div style={{ padding: '20px' }}>
      <h2>Upload Shipments CSV</h2>
      <input type="file" accept=".csv" onChange={handleFileChange} />
      <button onClick={handleUpload}>Upload & Process</button>

      {results.length > 0 && (
        <div style={{ marginTop: '20px' }}>
          <h3>Results</h3>
          {results.map((res, i) => (
            <pre key={i} style={{ background: '#f0f0f0', padding: '10px' }}>
              {JSON.stringify(res, null, 2)}
            </pre>
          ))}
        </div>
      )}
    </div>
  );
}

export default UploadPage;
