import React, { useState } from "react";
import "./Form.css";

function HtsForm() {
  const [description, setDescription] = useState("");
  const [country, setCountry] = useState("");
  const [result, setResult] = useState([]);

  const submit = async (e) => {
    e.preventDefault();
    try {
      // const response = await fetch("/api/hts/suggest"
        const response = await fetch("http://127.0.0.1:8000/api/hts/suggest",{
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ description, country_of_origin: country }),
      });
      const data = await response.json();
      setResult(data.suggestions || []);
    } catch (err) {
      console.error(err);
      setResult(["Server returned error"]);
    }
  };

  return (
    <div className="form-container">
      <h2>HTS Suggestion</h2>
      <form onSubmit={submit}>
        <label>Description</label>
        <input
          type="text"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          required
        />

        <label>Country of Origin</label>
        <input
          type="text"
          value={country}
          onChange={(e) => setCountry(e.target.value)}
          required
        />

        <button type="submit">Get Suggestions</button>
      </form>

      <div className="result">
        {result.length > 0 && (
          <ul>
            {result.map((item, idx) => (
              <li key={idx}>{item}</li>
            ))}
          </ul>
        )}
      </div>
    </div>
  );
}

export default HtsForm;
