from pydantic import BaseModel

class ValidationResult(BaseModel):
    valid: bool
    issues: list[str]