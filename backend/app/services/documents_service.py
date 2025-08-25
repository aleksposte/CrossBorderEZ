def process_document(document_name: str) -> str:
    """
    Process a document and return status.
    """
    processed = {"Invoice", "Bill of Lading"}
    return "Processed" if document_name in processed else "Pending"
