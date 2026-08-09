import re
from validator import validate_age, validate_email, validate_phone
class Student:
    def __init__(self, roll, name, age, department, email, phone):
        self.roll = roll
        self.name = name
        self.age = age
        self.department = department
        self.email = email
        self.phone = phone

    def display_details(self):
        print(f"Roll Number : {self.roll}")
        print(f"Name        : {self.name}")
        print(f"Age         : {self.age}")
        print(f"Department  : {self.department}")
        print(f"Email       : {self.email}")
        print(f"Phone       : {self.phone}")

    def update_department(self, department):
        if not department.strip():
            raise ValueError("Department cannot be empty.")
        self.department = department

    def __str__(self):
      return (
        f"Roll Number : {self.roll}\n"
        f"Name        : {self.name}\n"
        f"Age         : {self.age}\n"
        f"Department  : {self.department}\n"
        f"Email       : {self.email}\n"
        f"Phone       : {self.phone}"
    )
    
    @property
    def age(self):
       return self._age

    @age.setter
    def age(self, value):
        validate_age(value)
        self._age = value

    @property
    def phone(self):
       return self._phone

    @phone.setter
    def phone(self, value):
       validate_phone(value)
       self._phone = value  

    @property
    def email(self):
       return self._email

    @email.setter
    def email(self, value):
       validate_email(value)
       self._email = value

student = Student(
    101,
    "Sweety",
    19,
    "CSE",
    "sweety@gmail.com",
    "9876543210"
)

print(student)