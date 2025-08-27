from pydantic import BaseModel


class USMCACheckRequest(BaseModel):
    description: str
    hs_code: str
    country_of_origin: str


class USMCACheckResponse(BaseModel):
    status: str
    message: str
