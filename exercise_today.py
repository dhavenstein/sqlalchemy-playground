# Today's exercise!

"""
 Part 1:
 Create a new class called "Book". Note: No need to inherit from SQLAlchemy's Base just yet!
 It should have the following fields with sensible type annotations:
 - title
 - author
 - published_year
 - isbn
 - price
 - stock_quantity
 - is_available
"""

class Book:
    ... # TODO: Implement the Book class

"""
Part 2:
Implement the Book class as a SQLAlchemy model! You can name it BookModel.
For this, import the declarative_base class from sqlalchemy.orm,
and derive the class from it. Add Column fields for each of the attributes
so it is equivalent to the Book class from Part 1.
"""

... # TODO: Implement the BookModel class

"""
Part 3:
Implement a test for the BookModel class.

Open the file tests/test_exercise_today.py, and implement the following test cases:
- Test that the BookModel class can be instantiated
- Test that the BookModel class has the correct fields
- Test that the BookModel class can be saved to the database
- Test that the BookModel class can be loaded from the database via a query
- Test adding multiple books (say 10) to the database, and check that the number of books in the database is correct

Run the newly created tests with `uv run pytest tests/test_exercise_today.py`
"""

"""
Bonus:
- Implement a method to get the average price of all books in the database
- Implement a method to get the total stock quantity of all books in the database
- Implement a method to get the book with the highest stock quantity
- Implement a BookStore class, which has a relationship with the BookModel class:
  - It should have a name
  - It should have a location
  - It should have a list of books (many-to-many relationship with the BookModel class)
  - It should have a method to add a book to the store
  - It should have a method to remove a book from the store
  - It should have a method to get the total stock quantity of all books in the store

You can use exercise_3.py as a template for creating a many-to-many relationship with SQLAlchemy.
"""

... # TODO: Implement the BookStore class
