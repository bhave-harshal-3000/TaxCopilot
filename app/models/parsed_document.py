from sqlalchemy import Column, Integer, String, ForeignKey, JSON, UniqueConstraint

from app.database.database import Base


class ParsedDocument(Base):

    __tablename__ = "parsed_documents"

    __table_args__ = (
        UniqueConstraint("case_id", "document_type", name="uq_case_document_type"),
    )

    id = Column(Integer, primary_key=True, index=True)

    case_id = Column(Integer, ForeignKey("cases.id"))

    document_type = Column(String)

    parsed_json = Column(JSON)