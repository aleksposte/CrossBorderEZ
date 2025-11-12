import React from "react";
import HtsForm from "./components/HtsForm";
import UsmcaForm from "./components/UsmcaForm";
import BulkUpload from "./components/BulkUpload";
import "./App.css";

function App() {
  return (
    <div className="App">
      <h1>Crossborder EZ</h1>
      <section>
        <h2>HTS Suggestion</h2>
        <HtsForm />
      </section>
      <section>
        <h2>USMCA Check</h2>
        <UsmcaForm />
      </section>
      <section>
        <h2>Bulk CSV Upload</h2>
        <BulkUpload />
      </section>
    </div>
  );
}

export default App;
