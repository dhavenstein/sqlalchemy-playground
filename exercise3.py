from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from faker import Faker

Base = declarative_base()
fake = Faker()

# Association table for the many-to-many relationship.
student_courses = Table(
    'student_courses', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id')),
    Column('course_id', Integer, ForeignKey('courses.id'))
)

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)

    # Many-to-many: A student can enroll in multiple courses.
    courses = relationship("Course", secondary=student_courses, back_populates="students")

    def __repr__(self):
        return f"<Student(name='{self.name}')>"

    @classmethod
    def generate_fake(cls):
        """Generate a fake student."""
        return cls(name=fake.name())

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)

    # Many-to-many: A course can have multiple students.
    students = relationship("Student", secondary=student_courses, back_populates="courses")

    def __repr__(self):
        return f"<Course(title='{self.title}')>"

    @classmethod
    def generate_fake(cls):
        """Generate a fake course title."""
        return cls(title=fake.catch_phrase())