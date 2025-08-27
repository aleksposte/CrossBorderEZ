from pydantic import BaseModel


class HTSSuggestionRequest(BaseModel):
    description: str
    country_of_origin: str


class HTSSuggestionResponse(BaseModel):
    code: str
    description: str
