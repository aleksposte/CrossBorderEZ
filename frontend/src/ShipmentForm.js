import React, { useState } from "react";
import axios from "axios";

export default function ShipmentForm() {
  const [description, setDescription] = useState("");
  const [hsCode, setHsCode] = useState("");
  const [exporter, setExporter] = useState("");
  const [importer, setImporter] = useState("");
  const [country, setCountry] = useState("");
  const [shipmentId, setShipmentId] = useState("");
  const [result, setResult] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await axios.post("http://127.0.0.1:8000/api/workflow/process-shipment", {
        description,
        hs_code: hsCode,
        exporter_name: exporter,
        importer_name: importer,
        country_of_origin: country,
        shipment_id: shipmentId,
        certifier_name: "John Doe",
        certifier_signature: "JD",
        certifier_date: "2025-08-25",
        producer_name: "ACME Factory",
        documents: [],
      });
      setResult(res.data);
    } catch (err) {
      console.error(err);
      setResult({ error: "Failed to process shipment" });
    }
  };

  return (
    <div>
      <h2>Process Shipment</h2>
      <form onSubmit={handleSubmit}>
        <input placeholder="Description" value={description} onChange={(e) => setDescription(e.target.value)} />
        <input placeholder="HS Code" value={hsCode} onChange={(e) => setHsCode(e.target.value)} />
        <input placeholder="Exporter" value={exporter} onChange={(e) => setExporter(e.target.value)} />
        <input placeholder="Importer" value={importer} onChange={(e) => setImporter(e.target.value)} />
        <input placeholder="Country" value={country} onChange={(e) => setCountry(e.target.value)} />
        <input placeholder="Shipment ID" value={shipmentId} onChange={(e) => setShipmentId(e.target.value)} />
        <button type="submit">Process Shipment</button>
      </form>
      {result && (
        <div>
          {result.error ? result.error : `Shipment processed: ${JSON.stringify(result)}`}
        </div>
      )}
    </div>
  );
}
