from sqlalchemy import TIMESTAMP, Column, Integer, String
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base

Base: DeclarativeMeta = declarative_base()


class Level(Base):
    __tablename__ = 'level'
    id = Column(Integer, primary_key=True)
    winter = Column(String(2))
    summer = Column(String(2))
    autumn = Column(String(2))
    spring = Column(String(2))




