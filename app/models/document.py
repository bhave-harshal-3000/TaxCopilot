from sqlalchemy import Column, Integer, String, ForeignKey
from app.database.database import Base

class Document(Base):

    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    case_id = Column(Integer, ForeignKey("cases.id"))
    document_type = Column(String)
    filename = Column(String)
    filepath = Column(String)
    status = Column(String, default="Uploaded")