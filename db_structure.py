from sqlalchemy import Column, Integer, MetaData, String, CHAR, VARCHAR
from database import Base


metadata = MetaData()


class Trainee(Base):
    __tablename__ = "trainee"

    ID = Column(CHAR(5), primary_key=True)
    name = Column(VARCHAR(20), nullable=False)
    dept_name = Column(VARCHAR(20))
    second_name = Column(VARCHAR(20), nullable=False)

class Instructor(Base):
    __tablename__ = "instructor"

    ID = Column(CHAR(5), primary_key=True)
    name = Column(VARCHAR(20), nullable=False)
    dept_name = Column(VARCHAR(20))
    
