import React from "react";
import ShipmentForm from "./components/ShipmentForm";
import BulkUploadForm from "./components/BulkUploadForm";

const App: React.FC = () => {
  return (
    <div className="min-h-screen bg-gray-100 flex flex-col items-center justify-start p-6">
      <div className="bg-white p-8 rounded shadow w-full max-w-lg mb-6">
        <h1 className="text-2xl font-bold mb-4">Single Shipment</h1>
        <ShipmentForm />
      </div>

      <div className="bg-white p-8 rounded shadow w-full max-w-lg">
        <h1 className="text-2xl font-bold mb-4">Bulk Upload Shipments</h1>
        <BulkUploadForm />
      </div>
    </div>
  );
};

export default App;
