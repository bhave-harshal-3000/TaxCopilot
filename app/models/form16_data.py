from pydantic import BaseModel


class Form16Data(BaseModel):

    document_type: str
    employee_name: str | None = None
    employer: str | None = None
    pan: str | None = None
    salary: float | None = None
    tds: float | None = None
    financial_year: str | None = None