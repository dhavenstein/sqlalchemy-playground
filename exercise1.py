# exercise1.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from faker import Faker

Base = declarative_base()
fake = Faker()

class Country(Base):
    __tablename__ = 'countries'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    # One-to-one relationship: Each country has one capital.
    capital = relationship("Capital", uselist=False, back_populates="country")

    def __repr__(self):
        return f"<Country(name='{self.name}')>"

    @classmethod
    def generate_fake(cls, session):
        """Generate a fake country."""
        while True:
            country_name = fake.country()
            if session.query(Country).filter_by(name=country_name).first() is None:
                return cls(name=country_name)

class Capital(Base):
    __tablename__ = 'capitals'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    country_id = Column(Integer, ForeignKey('countries.id'))

    # One-to-one relationship: Each capital belongs to one country.
    country = relationship("Country", back_populates="capital")

    def __repr__(self):
        return f"<Capital(name='{self.name}')>"

    @classmethod
    def generate_fake(cls, session):
        """Generate a fake capital city."""
        while True:
            capital_name = fake.city()
            if session.query(Capital).filter_by(name=capital_name).first() is None:
                return cls(name=capital_name)