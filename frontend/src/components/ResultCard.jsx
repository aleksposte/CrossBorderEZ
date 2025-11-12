import React from "react";

export default function ResultCard({ data }) {
  if (data.error) return <div className="result error">{data.error}</div>;
  return (
    <div className="result">
      {data.code && <p>HTS Code: {data.code}</p>}
      {data.description && <p>Description: {data.description}</p>}
      {data.status && <p>Status: {data.status}</p>}
      {data.message && <p>Message: {data.message}</p>}
    </div>
  );
}
