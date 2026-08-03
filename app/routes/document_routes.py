import os
import shutil

from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session
from app.agents.parser_agent import ParserAgent
from app.database.database import get_db
from app.models.document import Document
from app.models.parsed_document import ParsedDocument
from fastapi import Form

router = APIRouter()

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post("/cases/{case_id}/documents")
def upload_document(
    case_id: int,
    file: UploadFile = File(...),
    document_type: str = Form(...),
    db: Session = Depends(get_db)
):

    case_folder = os.path.join(
        UPLOAD_FOLDER,
        f"case_{case_id}"
    )

    os.makedirs(case_folder, exist_ok=True)

    filepath = os.path.join(
        case_folder,
        file.filename
    )

    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    document = Document(
        case_id=case_id,
        filename=file.filename,
        filepath=filepath,
        document_type=document_type
    )

    db.add(document)
    db.commit()
    db.refresh(document)
    
    
    parsed = ParserAgent.parse(filepath,document_type)
    
    existing_document = (
        db.query(ParsedDocument)
        .filter(
            ParsedDocument.case_id == case_id,
            ParsedDocument.document_type == document_type
        )
        .first()
    )

    if existing_document:

        existing_document.parsed_json = parsed.model_dump()

    else:

        parsed_document = ParsedDocument(
            case_id=case_id,
            document_type=document_type,
            parsed_json=parsed.model_dump()
        )

        db.add(parsed_document)

    db.commit()


    return parsed.model_dump()