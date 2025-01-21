from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
import random
from models import Base, Student, Group, Teacher, Subject, Grade
from datetime import date, timedelta

DATABASE_URL = "postgresql://user:password@localhost/dbname"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()
faker = Faker()

def seed_data():
    groups = [Group(name=f"Group {i}") for i in range(1, 4)]
    session.add_all(groups)
    session.commit()

    teachers = [Teacher(fullname=faker.name()) for _ in range(5)]
    session.add_all(teachers)
    session.commit()

    subjects = [Subject(name=f"Subject {i}", teacher_id=random.choice(teachers).id) for i in range(1, 9)]
    session.add_all(subjects)
    session.commit()

    students = [Student(fullname=faker.name(), group_id=random.choice(groups).id) for _ in range(50)]
    session.add_all(students)
    session.commit()

    for student in students:
        for subject in subjects:
            grades = [
                Grade(student_id=student.id, subject_id=subject.id, grade=random.uniform(1, 12),
                    date_received=date.today() - timedelta(days=random.randint(1, 100)))
                for _ in range(20)
            ]
            session.add_all(grades)

    session.commit()

if __name__ == "__main__":
    seed_data()
