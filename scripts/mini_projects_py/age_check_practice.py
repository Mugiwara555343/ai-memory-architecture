age = int(input("What is your age? "))

if age >= 5:
    print(f"Ok, you're {age} years old ")

elif age >= 0 and age <= 4:
    print("I suspect you can't write quite yet...")

else:
    print("That must be a mistake")


age = int(input("What is your age? "))

if age < 0:

    print("That must be a mistake")

elif age < 5:

    print("I suspect you can't write quite yet...")

else:

    print(f"Ok, you're {age} years old")