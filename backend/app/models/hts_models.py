from pydantic import BaseModel


class HTSSuggestionResponse(BaseModel):
    query: str
    suggestions: list[str]
