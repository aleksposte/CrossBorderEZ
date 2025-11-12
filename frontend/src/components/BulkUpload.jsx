import React, { useState } from "react";
import "./Form.css";

const BulkUpload = () => {
  const [file, setFile] = useState(null);
  const [message, setMessage] = useState("");

  const submit = async (e) => {
    e.preventDefault();
    if (!file) return setMessage("Please select a CSV file");
    const formData = new FormData();
    formData.append("file", file);
    try {
      const response = await fetch("http://127.0.0.1:8000/api/process_csv", {
        method: "POST",
        body: formData,
      });
      if (!response.ok) throw new Error("Server returned error");
      const blob = await response.blob();
      const url = window.URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      a.download = "processed.zip";
      document.body.appendChild(a);
      a.click();
      a.remove();
      setMessage("ZIP file downloaded!");
    } catch (err) {
      console.error(err);
      setMessage("Error: " + err.message);
    }
  };
  return (
    <div className="form-container">
      <h2>Bulk Upload</h2>
      <form onSubmit={submit}>
        <input
          type="file"
          accept=".csv"
          onChange={(e) => setFile(e.target.files[0])}
        />
        <button type="submit">Upload CSV</button>
      </form>
      {message && <div className="result">{message}</div>}
    </div>
  );

};

export default BulkUpload;

