import random
from exercise3 import Student, Course

def test_exercise3(session):
    student = Student.generate_fake()
    course = Course.generate_fake()
    student.courses = [course]

    session.add(student)
    session.add(course)

    session.commit()

    assert session.query(Student).count() == 1
    assert session.query(Course).count() == 1

    assert session.query(Student).first().courses == [session.query(Course).first()]


def test_exercise3_generate_fake(session):
    for _ in range(10):
        student = Student.generate_fake()
        courses = [Course.generate_fake() for _ in range(random.randint(0, 30))]
        student.courses = courses

        session.add(student)

        # Check student has the correct number of courses
        assert len(student.courses) == len(courses)

    session.commit()

    assert session.query(Student).count() == 10

    for student in session.query(Student).all():
        assert len(student.courses) == len(student.courses)

    for course in session.query(Course).all():
        assert len(course.students) == len(course.students)