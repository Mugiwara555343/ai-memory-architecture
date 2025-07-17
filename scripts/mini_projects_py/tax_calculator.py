value_of_gift = int(input("Value of gift: "))

if value_of_gift < 5000:
    print("No tax!")

elif value_of_gift <= 25000:
    print(f"Amount of tax: {100 + (value_of_gift - 5000) * 0.08} euros")

elif value_of_gift <= 55000:
    print(f"Amount of tax: {1700 + (value_of_gift - 25000) * 0.10} euros")

elif value_of_gift <= 200000:
    print(f"Amount of tax: {4700 + (value_of_gift - 55000) * 0.12} euros")

elif value_of_gift <= 1000000:
    print(f"Amount of tax: {22100 + (value_of_gift - 200000) * 0.15} euros")

else:
    print(f"Amount of tax: {142100 + (value_of_gift - 1000000) * 0.17} euros")

value = int(input("Value of gift: "))

 
#Below was the solution given and is better written for readability
if value < 5000:

    tax = 0

elif value <= 25000:

    tax = 100 + (value - 5000) * 0.08

elif value <= 55000:

    tax = 1700 + (value - 25000) * 0.10

elif value <= 200000:

    tax = 4700 + (value - 55000) * 0.12

elif value <= 1000000:

    tax = 22100 + (value - 200000) * 0.15

else:

    tax = 142100 + (value - 1000000) * 0.17

 

if tax == 0:

    print("No tax!")

else:

    print(f"Amount of tax: {tax} euros")