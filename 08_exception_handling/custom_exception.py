# custom_exception.py

class AgeError(Exception):
    pass

try:
    age = int(input("Enter age: "))
    if age < 18:
        raise AgeError
    print("Eligible")
except AgeError:
    print("Age must be 18 or above")
