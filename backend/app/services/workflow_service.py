def get_workflow(process: str):
    workflows = {
        "import": ["document_check", "duty_calculation", "release"],
        "export": ["document_check", "compliance_validation", "shipping"],
    }
    return workflows.get(process, ["unknown_process"])
