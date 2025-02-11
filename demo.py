from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from faker import Faker

fake = Faker()

Base = declarative_base()

# Demo time :)
class Person:
    name : str
    age : int
    address : str
    phone_number : str
    email : str