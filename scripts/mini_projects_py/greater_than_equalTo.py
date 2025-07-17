num_1 = int(input("Please type in the first number: "))
num_2 = int(input("Please type in another number:  "))

if num_1 > num_2:
    print(f"The greater number was: {num_1}")
elif num_2 > num_1:
    print(f"The greater number was: {num_2}")
elif num_1 == num_2:
    print("The numbers are equal!")
