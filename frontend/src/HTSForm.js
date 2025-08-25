import React, { useState } from "react";
import axios from "axios";

export default function HTSForm() {
  const [description, setDescription] = useState("");
  const [country, setCountry] = useState("");
  const [result, setResult] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await axios.post("http://127.0.0.1:8000/api/hts/suggest", {
        description,
        country_of_origin: country,
      });
      setResult(res.data);
    } catch (err) {
      console.error(err);
      setResult({ error: "Failed to get HTS code" });
    }
  };

  return (
    <div>
      <h2>HTS Suggestion</h2>
      <form onSubmit={handleSubmit}>
        <input
          placeholder="Description"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
        />
        <input
          placeholder="Country"
          value={country}
          onChange={(e) => setCountry(e.target.value)}
        />
        <button type="submit">Get HTS Code</button>
      </form>
      {result && (
        <div>
          {result.error ? result.error : `${result.description}: ${result.code}`}
        </div>
      )}
    </div>
  );
}
