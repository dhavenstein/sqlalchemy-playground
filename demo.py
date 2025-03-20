from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Person(Base):
    __tablename__ = "person"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(50))
    age = Column(Integer)
    address = Column(String(255))
    phone_number = Column(String(20))
    email = Column(String(255))

    def __repr__(self):
        return f"Person(id={self.id}, name={self.name}, age={self.age}, address={self.address}, phone_number={self.phone_number}, email={self.email})"