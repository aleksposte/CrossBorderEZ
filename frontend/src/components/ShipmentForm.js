import React, { useState } from "react";
import axios from "axios";

const ShipmentForm = () => {
  const [description, setDescription] = useState("");
  const [hsCode, setHsCode] = useState("");
  const [exporter, setExporter] = useState("");
  const [importer, setImporter] = useState("");
  const [producer, setProducer] = useState("");
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");
    setResult(null);

    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/api/workflow/process-shipment",
        {
          exporter_name: exporter,
          importer_name: importer,
          producer_name: producer,
          description: description,
          hs_code: hsCode,
          country_of_origin: "USA",
          certifier_name: "John Doe",
          certifier_signature: "JD",
          certifier_date: new Date().toISOString().split("T")[0],
          documents: [],
          shipment_id: "SHP001",
        }
      );
      setResult(response.data);
    } catch (err) {
      console.error(err);
      setError(err.response?.data?.detail || "Ошибка обработки отправки");
    }
  };

  return (
    <div>
      <h2>Process Shipment</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Exporter name"
          value={exporter}
          onChange={(e) => setExporter(e.target.value)}
          required
        />
        <input
          type="text"
          placeholder="Importer name"
          value={importer}
          onChange={(e) => setImporter(e.target.value)}
          required
        />
        <input
          type="text"
          placeholder="Producer name"
          value={producer}
          onChange={(e) => setProducer(e.target.value)}
          required
        />
        <input
          type="text"
          placeholder="Product description"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          required
        />
        <input
          type="text"
          placeholder="HS Code"
          value={hsCode}
          onChange={(e) => setHsCode(e.target.value)}
          required
        />
        <button type="submit">Process Shipment</button>
      </form>

      {result && (
        <div>
          <h3>Result</h3>
          <p>{result.message}</p>
        </div>
      )}

      {error && <p style={{ color: "red" }}>{error}</p>}
    </div>
  );
};

export default ShipmentForm;
