# nested_if.py
# Check eligibility to vote

age = int(input("Enter your age: "))

if age >= 18:
    if age >= 60:
        print("You are eligible to vote (Senior Citizen)")
    else:
        print("You are eligible to vote")
else:
    print("You are not eligible to vote")
