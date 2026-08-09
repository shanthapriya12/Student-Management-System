# Student Management System

A console-based **Student Management System** built with Python and SQLite. The project demonstrates CRUD operations, object-oriented programming, input validation, modular programming, and database management.

## 🚀 Features

* ➕ Add new students
* 📋 View all students
* 🔍 Search students by roll number
* ✏️ Update student information
* 🗑️ Delete student records
* ✅ Validate student name, age, email, and phone number
* 💾 Store student records permanently using SQLite
* 🧱 Object-oriented `Student` model
* 🧩 Modular project structure
* ⚠️ Error handling using Python exceptions

## 🛠️ Technologies Used

| Technology | Purpose                                    |
| ---------- | ------------------------------------------ |
| Python     | Main programming language                  |
| SQLite     | Database management                        |
| `re`       | Input validation using regular expressions |
| OOP        | Student model and data organization        |
| Git        | Version control                            |
| GitHub     | Source code hosting                        |

## 📁 Project Structure

```text
Student-Management-System/
│
├── main.py
├── database.py
├── models.py
├── validator.py
├── requirements.txt
├── README.md
└── .gitignore
```

### `main.py`

Contains the main program and menu system.

It handles:

* Adding students
* Viewing students
* Searching students
* Updating students
* Deleting students
* Exiting the application

### `database.py`

Handles SQLite database operations such as:

* Creating the `students` table
* Inserting student records
* Retrieving students
* Searching by roll number
* Updating student information
* Deleting student records

### `models.py`

Contains the `Student` class and demonstrates object-oriented programming.

The class includes:

* Student attributes
* Properties and setters
* Age validation
* Email validation
* Phone validation
* Student information display

### `validator.py`

Contains validation functions for checking:

* Names
* Ages
* Email addresses
* Phone numbers

## 🗄️ Database

The application uses an SQLite database named:

```text
college.db
```

The `students` table contains:

```text
roll
name
age
department
email
phone
```

The database file is excluded from Git using `.gitignore`.

## ▶️ How to Run

Make sure Python is installed.

Clone the repository:

```bash
git clone https://github.com/shanthapriya12/Student-Management-System.git
```

Move into the project directory:

```bash
cd Student-Management-System
```

Run the application:

```bash
python main.py
```

The application will display a menu:

```text
1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit
```

## 🔄 CRUD Operations

This project implements the four basic database operations:

* **Create** → Add student
* **Read** → View and search students
* **Update** → Modify student information
* **Delete** → Remove student records

## 🎯 Learning Objectives

This project was developed to practice:

* Python functions
* Classes and objects
* Encapsulation
* Properties and setters
* Exception handling
* Regular expressions
* SQLite database operations
* SQL queries
* Modular programming
* Git and GitHub

## 📌 Future Improvements

Possible future improvements include:

* Graphical user interface
* Login/authentication system
* Student attendance management
* Marks and grade management
* Export student data to CSV
* Advanced search and filtering

## 👩‍💻 Author

**Shanthapriya**

Computer Science Student
