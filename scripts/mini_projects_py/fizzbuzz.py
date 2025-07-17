number = int(input("Please enter an integer: "))

if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")

elif number % 3 == 0:
    print("Fizz")

elif number % 5 == 0:
    print("Buzz")