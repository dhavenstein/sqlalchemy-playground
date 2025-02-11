import pytest
from sqlalchemy import create_engine
from demo import Base
from sqlalchemy.orm import sessionmaker

@pytest.fixture
def demo_session():
    engine = create_engine('sqlite:///:memory:', echo=True)
    Base.metadata.create_all(engine)
    session_maker = sessionmaker(bind=engine)
    session = session_maker()
    yield session
    session.close()


def test_demo(demo_session):
    # Do stuff with demo class :)
    ...