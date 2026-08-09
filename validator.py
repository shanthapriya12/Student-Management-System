import re


def validate_name(name):
    if not name.replace(" ", "").isalpha():
        raise ValueError("Invalid name.")
    return True


def validate_age(age):
    if age < 16 or age > 100:
        raise ValueError("Age must be between 16 and 100.")
    return True


def validate_email(email):
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        raise ValueError("Invalid email format.")
    return True


def validate_phone(phone):
    if not re.match(r"^\d{10}$", phone):
        raise ValueError("Phone number must contain exactly 10 digits.")
    return True