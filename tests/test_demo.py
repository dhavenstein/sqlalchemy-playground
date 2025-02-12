import pytest
from sqlalchemy import create_engine
from demo import Base, Person, fake
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
    for _ in range(10):
        person = Person(
            name=fake.name(),
            age=fake.random_int(min=18, max=80),
            address=fake.address(),
            phone_number=fake.phone_number(),
            email=fake.email()
        )
        demo_session.add(person)
    demo_session.commit()

    # Query persons under 50
    people_under_50 = demo_session.query(Person).filter(Person.age > 50).all()
    for person in people_under_50:
        print(person)