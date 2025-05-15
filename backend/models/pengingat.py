from sqlalchemy import Column, Integer, String, Date
from .meta import Base

class Pengingat(Base):
    __tablename__ = 'pengingat'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    nama = Column(String)
    tanggal = Column(Date)
    frekuensi = Column(String) 