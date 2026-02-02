# finally.py

try:
    file = open("data.txt", "r")
    print(file.read())
except:
    print("File error")
finally:
    print("Program completed")
