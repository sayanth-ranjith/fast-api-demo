from sqlalchemy import Integer, String, BigInteger, Column
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass

class CustomerDetails(Base):
    __tablename__ = "cpd_bank_tbl"

    id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    address = Column(String)
    country = Column(String)
    state = Column(String)
    pincode = Column(Integer)
    gender = Column(String)
    accountnumber = Column(BigInteger)