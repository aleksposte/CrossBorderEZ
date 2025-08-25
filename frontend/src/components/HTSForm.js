import React, { useState } from 'react';
import { getHTSCode } from '../api';

export default function HTSForm() {
  const [description, setDescription] = useState('');
  const [result, setResult] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const data = await getHTSCode(description);
    setResult(data);
  };

  return (
    <div style={{ marginTop: '20px' }}>
      <h2>HTS Suggestion</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          placeholder="Item description"
          required
        />
        <button type="submit">Suggest HTS</button>
      </form>
      {result && (
        <div>
          <p>Code: {result.code}</p>
          <p>Description: {result.description}</p>
        </div>
      )}
    </div>
  );
}
