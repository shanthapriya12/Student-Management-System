from database import (
    create_table,
    insert_student,
    get_all_students,
    search_student_by_roll,
    update_student_data,
    delete_student_by_roll
)
from models import Student
print("=" * 40)
print(" STUDENT MANAGEMENT SYSTEM ")
print("=" * 40)
print("1. Add Students\n2. View Students\n3. Search Student\n4. Update Student\n5. Delete Student\n6. Exit")
create_table()
def add_student():
    try:
        roll = int(input("Enter roll number: "))

        if roll <= 0:
            print("Roll number must be positive.")
            return

        if search_student_by_roll(roll):
            print("Roll number already exists.")
            return

        name = input("Enter name: ")
        age = int(input("Enter age: "))
        department = input("Enter department: ")
        email = input("Enter email: ")
        phone = input("Enter phone number: ")

        student = Student(
            roll,
            name,
            age,
            department,
            email,
            phone
        )

    except ValueError as e:
        print(e)
        return

    added = insert_student(
    student.roll,
    student.name,
    student.age,
    student.department,
    student.email,
    student.phone
)

    if added:
        print("Student added successfully!")
    else:
        print("Student could not be added.")

def view_students():
    students = get_all_students()

    if not students:
        print("No students found.")
        return

    print("=" * 40)
    print(" STUDENT LIST ")
    print("=" * 40)

    for student in students:
      print(student)
      print("-" * 40)
    
def search_student():
    try:
       roll = int(input("Enter roll number: "))
    except ValueError:
       print("Please enter a valid number.")
       return


    student = search_student_by_roll(roll)

    if student:
        student.display_details()
    else:
        print("Student not found.")

def update_student():
    try:
        roll = int(input("Enter roll number: "))
    except ValueError:
           print("Please enter a valid number.")
           return

    student = search_student_by_roll(roll)

    if not student:
        print("Student not found.")
        return

    print("1. Name")
    print("2. Age")
    print("3. Department")
    print("4. Email")
    print("5. Phone")
    print("6. Cancel")

    choice = input("What do you want to update? ")

    if choice == "1":
        field = "name"
        print(f"Current name: {student.name}")

    elif choice == "2":
        field = "age"
        print(f"Current age: {student.age}")

    elif choice == "3":
        field = "department"
        print(f"Current department: {student.department}")

    elif choice == "4":
        field = "email"
        print(f"Current email: {student.email}")

    elif choice == "5":
        field = "phone"
        print(f"Current phone: {student.phone}")

    elif choice == "6":
        print("Update cancelled.")
        return

    else:
        print("Invalid choice.")
        return

    value = input("Enter new value: ")

    try:
        if field == "age":
            value = int(value)
            student.age = value

        elif field == "email":
            student.email = value

        elif field == "phone":
            student.phone = value

        elif field == "name":
            student.name = value

        elif field == "department":
            student.department = value

    except ValueError as e:
        print(e)
        return

    updated = update_student_data(roll, field, value)

    if updated:
        print("Student updated successfully.")
    else:
        print("Student could not be updated.")
   
def delete_student():
    try:
           roll = int(input("Enter roll number: "))
    except ValueError:
           print("Please enter a valid number.")
           return
    student = search_student_by_roll(roll)

    if not student:
        print("Student not found.")
        return

    print(f"Name: {student.name}")
    print(f"Department: {student.department}")

    choice = input("Are you sure you want to delete this student? (y/n): ")

    if choice.lower() == "y":
        deleted = delete_student_by_roll(roll)

        if deleted:
            print("Student deleted successfully.")
        else:
            print("Student could not be deleted.")

    elif choice.lower() == "n":
        print("Deletion cancelled.")

    else:
        print("Invalid choice.")

def main():
 create_table()
 while True:
    print("=" * 40)
    print(" STUDENT MANAGEMENT SYSTEM ")
    print("=" * 40)

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Opening Add Student Menu...")
        add_student()

    elif choice == "2":
        print("Opening View Student Menu...")
        view_students()

    elif choice == "3":
        print("Opening Search Student Menu...")
        search_student()

    elif choice == "4":
        print("Opening Update Student Menu...")
        update_student()

    elif choice == "5":
        print("Opening Delete Student Menu...")
        delete_student()

    elif choice == "6":
        print("Thank you for using Student Management System!")
        break

    else:
        print("Invalid choice. Please try again.")
        
if __name__ == "__main__":
    main()