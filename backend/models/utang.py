from sqlalchemy import Column, Integer, String, Float, Date
from .meta import Base

class Utang(Base):
    __tablename__ = 'utang'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    pihak = Column(String) 
    jumlah = Column(Float)
    status = Column(String)
    tanggal = Column(Date)