# # backend/app/schemas/usmca.py
# from pydantic import BaseModel


# # -----------------------
# # HTS Suggestion
# # -----------------------
# class HTSSuggestionRequest(BaseModel):
#     description: str
#     country_of_origin: str


# class HTSSuggestionResponse(BaseModel):
#     code: str
#     description: str


# # -----------------------
# # USMCA Check
# # -----------------------
# class USMCACheckRequest(BaseModel):
#     description: str
#     hs_code: str
#     country_of_origin: str


# class USMCACheckResponse(BaseModel):
#     status: str  # "compliant" or "non-compliant"
#     explanation: str


from pydantic import BaseModel


class USMCACheckRequest(BaseModel):
    description: str
    hs_code: str
    country_of_origin: str


class USMCACheckResponse(BaseModel):
    status: str
    explanation: str
