from exercise1 import Country, Capital

def test_exercise1(session):
    # Create a country and a capital
    country = Country(name="France")
    capital = Capital(name="Paris")

    # Add the country and capital to the session
    session.add(country)
    session.add(capital)

    # Commit the changes to the database
    session.commit()

    assert session.query(Country).filter_by(name="France").first() is not None
    assert session.query(Capital).filter_by(name="Paris").first() is not None

def test_exercise1_generate_fake(session):
    for _ in range(10):
            country = Country.generate_fake(session)
            capital = Capital.generate_fake(session)

            session.add(country)
            session.add(capital)

    session.commit()

    assert session.query(Country).count() == 10
    assert session.query(Capital).count() == 10
