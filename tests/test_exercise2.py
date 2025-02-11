from exercise2 import Customer, Order
import random

def test_exercise2(session):
    customer = Customer.generate_fake()
    order = Order.generate_fake()
    customer.orders = [order]

    session.add(customer)
    session.add(order)

    session.commit()

    assert session.query(Customer).count() == 1
    assert session.query(Order).count() == 1

    assert session.query(Customer).first().orders == [session.query(Order).first()]

def test_exercise2_generate_fake(session):
    for _ in range(10):
        customer = Customer.generate_fake()
        orders = [Order.generate_fake() for _ in range(random.randint(0, 30))]
        customer.orders = orders

        session.add(customer)

        # Check customer has the correct number of orders
        assert len(customer.orders) == len(orders)

    session.commit()

    assert session.query(Customer).count() == 10