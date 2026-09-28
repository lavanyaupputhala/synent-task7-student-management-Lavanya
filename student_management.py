import json
import os

FILE_NAME = "students.json"


def load_students():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


def add_student(students):
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    age = input("Enter Student Age: ")
    course = input("Enter Student Course: ")

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)
    save_students(students)

    print("Student added successfully!")


def view_students(students):
    if not students:
        print("No student records found.")
        return

    print("\n===== STUDENT RECORDS =====")

    for student in students:
        print("ID:", student["id"])
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Course:", student["course"])
        print("--------------------------")


def update_student(students):
    student_id = input("Enter Student ID to update: ")

    for student in students:
        if student["id"] == student_id:
            student["name"] = input("Enter new name: ")
            student["age"] = input("Enter new age: ")
            student["course"] = input("Enter new course: ")

            save_students(students)

            print("Student updated successfully!")
            return

    print("Student not found.")


def delete_student(students):
    student_id = input("Enter Student ID to delete: ")

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            save_students(students)

            print("Student deleted successfully!")
            return

    print("Student not found.")


students = load_students()

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_student(students)

    elif choice == "2":
        view_students(students)

    elif choice == "3":
        update_student(students)

    elif choice == "4":
        delete_student(students)

    elif choice == "5":
        print("Thank you for using Student Management System!")
        break

    else:
        print("Invalid choice! Please choose between 1 and 5.")