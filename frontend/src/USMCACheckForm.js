import React, { useState } from "react";
import axios from "axios";

export default function USMCACheckForm() {
  const [description, setDescription] = useState("");
  const [hsCode, setHsCode] = useState("");
  const [country, setCountry] = useState("");
  const [result, setResult] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await axios.post("http://127.0.0.1:8000/api/usmca/check", {
        description,
        hs_code: hsCode,
        country_of_origin: country,
      });
      setResult(res.data);
    } catch (err) {
      console.error(err);
      setResult({ error: "Failed to check USMCA compliance" });
    }
  };

  return (
    <div>
      <h2>USMCA Check</h2>
      <form onSubmit={handleSubmit}>
        <input
          placeholder="Description"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
        />
        <input
          placeholder="HS Code"
          value={hsCode}
          onChange={(e) => setHsCode(e.target.value)}
        />
        <input
          placeholder="Country"
          value={country}
          onChange={(e) => setCountry(e.target.value)}
        />
        <button type="submit">Check Compliance</button>
      </form>
      {result && (
        <div>
          {result.error ? result.error : `${result.status}: ${result.explanation}`}
        </div>
      )}
    </div>
  );
}
