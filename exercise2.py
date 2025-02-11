from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from faker import Faker

Base = declarative_base()
fake = Faker()

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)

    # One-to-many relationship: One customer can have many orders.
    orders = relationship("Order", back_populates="customer")

    def __repr__(self):
        return f"<Customer(name='{self.name}')>"

    @classmethod
    def generate_fake(cls):
        """Generate a fake customer."""
        return cls(name=fake.name())

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    description = Column(String(100), nullable=False)
    customer_id = Column(Integer, ForeignKey('customers.id'))

    # Each order is linked to one customer.
    customer = relationship("Customer", back_populates="orders")

    def __repr__(self):
        return f"<Order(description='{self.description}')>"

    @classmethod
    def generate_fake(cls):
        """Generate a fake order description."""
        return cls(description=fake.sentence(nb_words=5))