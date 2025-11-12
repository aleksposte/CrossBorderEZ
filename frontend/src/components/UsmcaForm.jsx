import React, { useState } from "react";
import "./UsmcaForm.css"; // стили для формы

export default function UsmcaForm() {
  const [description, setDescription] = useState("");
  const [hsCode, setHsCode] = useState("");
  const [country, setCountry] = useState("");
  const [usmcaResult, setUsmcaResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const submit = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      const response = await fetch("http://127.0.0.1:8000/api/usmca/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          description: description,
          hs_code: hsCode,
          country_of_origin: country,
        }),
      });

      // Проверяем, что backend вернул JSON
      const text = await response.text();
      let result;
      try {
        result = JSON.parse(text);
      } catch (err) {
        console.error("Invalid JSON from server:", text);
        setLoading(false);
        return;
      }

      setUsmcaResult(result);
    } catch (error) {
      console.error("Error submitting USMCA:", error);
    }
    setLoading(false);
  };

  return (
    <div className="usmca-form-container">
      <h2>USMCA Compliance Check</h2>
      <form onSubmit={submit} className="usmca-form">
        <label>
          Description:
          <input
            type="text"
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            required
          />
        </label>
        <label>
          HS Code:
          <input
            type="text"
            value={hsCode}
            onChange={(e) => setHsCode(e.target.value)}
            required
          />
        </label>
        <label>
          Country of Origin:
          <input
            type="text"
            value={country}
            onChange={(e) => setCountry(e.target.value)}
            required
          />
        </label>
        <button type="submit" disabled={loading}>
          {loading ? "Checking..." : "Check USMCA"}
        </button>
      </form>

      {usmcaResult && (
        <div className="result">
          <p>Status: {usmcaResult.status}</p>
          <p>Message: {usmcaResult.message}</p>
        </div>
      )}
    </div>
  );
}
