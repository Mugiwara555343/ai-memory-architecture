print("Person 1:")
Name_1 = input("Name: ")
Age_1 = int(input("Age: "))

print("Person 2:")
Name_2 = input("Name: ")
Age_2 = int(input("Age: "))

if Age_1 > Age_2:
    print("The elder is", Name_1)
elif Age_2 > Age_1:
    print("The elder is", Name_2)
else:
    print(f"{Name_1} and {Name_2} are the same age")

