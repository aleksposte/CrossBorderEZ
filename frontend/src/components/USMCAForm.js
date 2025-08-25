import React, { useState } from "react";
import axios from "axios";

const USMCACheckForm = () => {
  const [description, setDescription] = useState("");
  const [country, setCountry] = useState("USA");
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");
    setResult(null);

    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/api/usmca/check",
        {
          description,
          country_of_origin: country,
        }
      );
      setResult(response.data);
    } catch (err) {
      console.error(err);
      setError(err.response?.data?.detail || "Ошибка USMCA проверки");
    }
  };

  return (
    <div>
      <h2>USMCA Compliance Check</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Enter product description"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          required
        />
        <select
          value={country}
          onChange={(e) => setCountry(e.target.value)}
        >
          <option value="USA">USA</option>
          <option value="CAN">Canada</option>
        </select>
        <button type="submit">Check Compliance</button>
      </form>

      {result && (
        <div>
          <h3>Result</h3>
          <p>Status: {result.status}</p>
        </div>
      )}

      {error && <p style={{ color: "red" }}>{error}</p>}
    </div>
  );
};

export default USMCACheckForm;
