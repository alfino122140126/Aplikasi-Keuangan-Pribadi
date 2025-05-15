from sqlalchemy import Column, Integer, String, Float, Date
from .meta import Base

class Transaksi(Base):
    __tablename__ = 'transaksi'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    kategori = Column(String)
    jumlah = Column(Float)
    tanggal = Column(Date)
    keterangan = Column(String)