# inheritance.py

class Person:
    def walk(self):
        print("Person is walking")

class Student(Person):
    def study(self):
        print("Student is studying")

s = Student()
s.walk()
s.study()
