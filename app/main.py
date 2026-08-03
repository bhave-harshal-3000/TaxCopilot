from fastapi import FastAPI
from app.database.database import Base, engine
from app.models.case import TaxCase
from app.models.document import Document
from app.models.parsed_document import ParsedDocument

from app.routes.case_routes import router as case_routes
from app.routes.document_routes import router as document_routes
from app.routes.validation_routes import router as validation_routes
from app.routes.calculation_routes import router as calculation_routes


app = FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(case_routes)
app.include_router(document_routes)

app.include_router(validation_routes)
app.include_router(calculation_routes)

@app.get("/")
def home():

    return {
        "message": "AI Tax Copilot Running"
    }