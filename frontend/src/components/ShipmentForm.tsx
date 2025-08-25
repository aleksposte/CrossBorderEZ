import React, { useState } from "react";
import axios from "axios";

interface WorkflowResponse {
  usmca_status: string;
  hts_code: string;
  documents_zip: string;
  risk_score: number;
  issues: string[];
}

const ShipmentForm: React.FC = () => {
  const [form, setForm] = useState({
    shipment_id: "",
    description: "",
    exporter_name: "",
    importer_name: "",
    producer_name: "",
    hs_code: "",
    country_of_origin: "",
    certifier_name: "",
    certifier_signature: "",
    certifier_date: "",
  });

  const [result, setResult] = useState<WorkflowResponse | null>(null);
  const [loading, setLoading] = useState(false);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    try {
      const res = await axios.post<WorkflowResponse>(
        "http://127.0.0.1:8000/api/workflow/process-shipment",
        form
      );
      setResult(res.data);
    } catch (err) {
      console.error(err);
      alert("Error processing shipment");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit} className="space-y-4">
        <input
          type="text"
          name="shipment_id"
          placeholder="Shipment ID"
          value={form.shipment_id}
          onChange={handleChange}
          className="w-full p-2 border rounded"
          required
        />
        <input
          type="text"
          name="description"
          placeholder="Product Description"
          value={form.description}
          onChange={handleChange}
          className="w-full p-2 border rounded"
          required
        />
        <input
          type="text"
          name="exporter_name"
          placeholder="Exporter Name"
          value={form.exporter_name}
          onChange={handleChange}
          className="w-full p-2 border rounded"
        />
        <input
          type="text"
          name="importer_name"
          placeholder="Importer Name"
          value={form.importer_name}
          onChange={handleChange}
          className="w-full p-2 border rounded"
        />
        <button
          type="submit"
          className="w-full bg-blue-600 text-white p-2 rounded"
          disabled={loading}
        >
          {loading ? "Processing..." : "Submit"}
        </button>
      </form>

      {result && (
        <div className="mt-6 p-4 bg-gray-50 border rounded space-y-2">
          <p><strong>USMCA Status:</strong> {result.usmca_status}</p>
          <p><strong>HTS Code:</strong> {result.hts_code}</p>
          <p><strong>Risk Score:</strong> {result.risk_score}</p>
          {result.issues.length > 0 && (
            <p><strong>Issues:</strong> {result.issues.join(", ")}</p>
          )}
          <a
            href={result.documents_zip}
            target="_blank"
            rel="noopener noreferrer"
            className="text-blue-600 underline mt-2 inline-block"
          >
            Download ZIP
          </a>
        </div>
      )}
    </div>
  );
};

export default ShipmentForm;
