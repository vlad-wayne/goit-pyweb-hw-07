import argparse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Student, Group, Teacher, Subject, Grade

DATABASE_URL = "postgresql://user:password@localhost/dbname"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

def create_teacher(name):
    teacher = Teacher(fullname=name)
    session.add(teacher)
    session.commit()
    print(f"Teacher '{name}' created successfully.")

def list_teachers():
    teachers = session.query(Teacher).all()
    for teacher in teachers:
        print(f"{teacher.id}: {teacher.fullname}")

def update_teacher(teacher_id, name):
    teacher = session.query(Teacher).get(teacher_id)
    if teacher:
        teacher.fullname = name
        session.commit()
        print(f"Teacher with ID {teacher_id} updated successfully.")
    else:
        print(f"Teacher with ID {teacher_id} not found.")

def delete_teacher(teacher_id):
    teacher = session.query(Teacher).get(teacher_id)
    if teacher:
        session.delete(teacher)
        session.commit()
        print(f"Teacher with ID {teacher_id} deleted successfully.")
    else:
        print(f"Teacher with ID {teacher_id} not found.")


def handle_action(args):
    if args.model == "Teacher":
        if args.action == "create":
            create_teacher(args.name)
        elif args.action == "list":
            list_teachers()
        elif args.action == "update":
            update_teacher(args.id, args.name)
        elif args.action == "remove":
            delete_teacher(args.id)
        else:
            print("Invalid action for Teacher.")
    elif args.model == "Group":
        
        pass
    elif args.model == "Student":
        
        pass
    elif args.model == "Subject":
        
        pass
    elif args.model == "Grade":
        
        pass
    else:
        print("Invalid model.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CLI for CRUD operations with the database.")
    parser.add_argument("-a", "--action", required=True, choices=["create", "list", "update", "remove"],
                        help="Action to perform: create, list, update, remove.")
    parser.add_argument("-m", "--model", required=True, choices=["Teacher", "Group", "Student", "Subject", "Grade"],
                        help="Model to perform the action on.")
    parser.add_argument("--id", type=int, help="ID of the record to update or delete.")
    parser.add_argument("-n", "--name", help="Name of the entity (e.g., teacher, group).")

    args = parser.parse_args()
    handle_action(args)
