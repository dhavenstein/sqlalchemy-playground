import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from exercise1 import Base as Base1
from exercise2 import Base as Base2
from exercise3 import Base as Base3

@pytest.fixture
def session():
    engine = create_engine('sqlite:///:memory:', echo=True)
    Base1.metadata.create_all(engine)
    Base2.metadata.create_all(engine)
    Base3.metadata.create_all(engine)
    session_maker = sessionmaker(bind=engine)
    session = session_maker()
    yield session
    session.close()
