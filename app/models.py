from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
import datetime

DBSession = scoped_session(sessionmaker())
Base = declarative_base()

class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    amount = Column(Float)
    category = Column(String)
    description = Column(String)
    date = Column(Date, default=datetime.date.today)
