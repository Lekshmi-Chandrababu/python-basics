# polymorphism.py

class Bird:
    def sound(self):
        print("Bird makes sound")

class Crow(Bird):
    def sound(self):
        print("Crow says caw caw")

b = Crow()
b.sound()
