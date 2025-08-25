import React from "react";
import HTSForm from "./HTSForm";
import USMCACheckForm from "./USMCACheckForm";
import ShipmentForm from "./ShipmentForm";

function App() {
  return (
    <div className="App">
      <h1>CrossBorder EZ</h1>
      <HTSForm />
      <USMCACheckForm />
      <ShipmentForm />
    </div>
  );
}

export default App;
