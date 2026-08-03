from sqlalchemy import Column, Integer, String

from app.database.database import Base


class TaxCase(Base):

    __tablename__ = "cases"

    id = Column(Integer, primary_key=True, index=True)

    client_name = Column(String)

    financial_year = Column(String)

    status = Column(String, default="Created")