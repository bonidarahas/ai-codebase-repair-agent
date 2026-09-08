from pydantic import BaseModel, Field


class RepositoryScanRequest(BaseModel):
    path: str = Field(min_length=1)


class RepositoryScanResponse(BaseModel):
    language: str
    framework: str | None
    files: int
    tests_found: bool