from flask import Flask, render_template, request, redirect, url_for

from database import (
    create_table,
    insert_student,
    get_all_students,
    search_student_by_roll,
    update_student_data,
    delete_student_by_roll
)

from models import Student


app = Flask(__name__)

create_table()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/students")
def view_students():
    students = get_all_students()
    return render_template("students.html", students=students)


@app.route("/add", methods=["GET", "POST"])
def add_student():

    if request.method == "POST":

        try:
            roll = int(request.form["roll"])
            name = request.form["name"]
            age = int(request.form["age"])
            department = request.form["department"]
            email = request.form["email"]
            phone = request.form["phone"]

            student = Student(
                roll,
                name,
                age,
                department,
                email,
                phone
            )

            if search_student_by_roll(roll):
                return "Roll number already exists."

            insert_student(
                student.roll,
                student.name,
                student.age,
                student.department,
                student.email,
                student.phone
            )

            return redirect(url_for("view_students"))

        except ValueError as e:
            return str(e)

    return render_template("add_student.html")


@app.route("/search", methods=["GET", "POST"])
def search_student():

    student = None

    if request.method == "POST":

        try:
            roll = int(request.form["roll"])
            student = search_student_by_roll(roll)

            if not student:
                return render_template(
                    "search.html",
                    student=None,
                    message="Student not found."
                )

        except ValueError:
            return render_template(
                "search.html",
                student=None,
                message="Please enter a valid roll number."
            )

    return render_template(
        "search.html",
        student=student
    )


@app.route("/update/<int:roll>", methods=["GET", "POST"])
def update_student(roll):

    student = search_student_by_roll(roll)

    if not student:
        return "Student not found."

    if request.method == "POST":

        try:
            name = request.form["name"]
            age = int(request.form["age"])
            department = request.form["department"]
            email = request.form["email"]
            phone = request.form["phone"]

            updated_student = Student(
                roll,
                name,
                age,
                department,
                email,
                phone
            )

            update_student_data(
                roll,
                "name",
                updated_student.name
            )

            update_student_data(
                roll,
                "age",
                updated_student.age
            )

            update_student_data(
                roll,
                "department",
                updated_student.department
            )

            update_student_data(
                roll,
                "email",
                updated_student.email
            )

            update_student_data(
                roll,
                "phone",
                updated_student.phone
            )

            return redirect(url_for("view_students"))

        except ValueError as e:
            return str(e)

    return render_template(
        "update_student.html",
        student=student
    )


@app.route("/delete/<int:roll>", methods=["POST"])
def delete_student(roll):

    student = search_student_by_roll(roll)

    if not student:
        return "Student not found."

    delete_student_by_roll(roll)

    return redirect(url_for("view_students"))


if __name__ == "__main__":
    app.run(debug=True)