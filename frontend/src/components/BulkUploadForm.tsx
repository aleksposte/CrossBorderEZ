import React, { useState } from "react";
import Papa from "papaparse";
import axios from "axios";

interface Shipment {
  shipment_id: string;
  description: string;
  exporter_name: string;
  importer_name: string;
  producer_name: string;
  hs_code: string;
  country_of_origin: string;
  certifier_name: string;
  certifier_signature: string;
  certifier_date: string;
}

interface WorkflowResponse {
  shipment_id: string;
  usmca_status: string;
  hts_code: string;
  documents_zip: string;
  risk_score: number;
  issues: string[];
}

const BulkUploadForm: React.FC = () => {
  const [file, setFile] = useState<File | null>(null);
  const [results, setResults] = useState<WorkflowResponse[]>([]);
  const [loading, setLoading] = useState(false);

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files) setFile(e.target.files[0]);
  };

  const handleUpload = () => {
    if (!file) return alert("Please select a CSV file");

    setLoading(true);
    Papa.parse<Shipment>(file, {
      header: true,
      skipEmptyLines: true,
      complete: async (parsed) => {
        const resArr: WorkflowResponse[] = [];
        for (const shipment of parsed.data) {
          try {
            const res = await axios.post<WorkflowResponse>(
              "http://127.0.0.1:8000/api/workflow/process-shipment",
              shipment
            );
            resArr.push(res.data);
          } catch (err) {
            console.error("Error processing shipment:", shipment.shipment_id, err);
          }
        }
        setResults(resArr);
        setLoading(false);
      },
    });
  };

  return (
    <div className="mt-6">
      <input type="file" accept=".csv" onChange={handleFileChange} />
      <button
        onClick={handleUpload}
        disabled={loading}
        className="ml-2 bg-green-600 text-white px-4 py-2 rounded"
      >
        {loading ? "Processing..." : "Upload CSV"}
      </button>

      {results.length > 0 && (
        <div className="mt-4 space-y-4">
          {results.map((r) => (
            <div key={r.shipment_id} className="p-2 border rounded bg-gray-50">
              <p><strong>Shipment:</strong> {r.shipment_id}</p>
              <p><strong>USMCA Status:</strong> {r.usmca_status}</p>
              <p><strong>HTS Code:</strong> {r.hts_code}</p>
              <p><strong>Risk Score:</strong> {r.risk_score}</p>
              {r.issues.length > 0 && (
                <p><strong>Issues:</strong> {r.issues.join(", ")}</p>
              )}
              <a
                href={r.documents_zip}
                target="_blank"
                rel="noopener noreferrer"
                className="text-blue-600 underline"
              >
                Download ZIP
              </a>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default BulkUploadForm;
