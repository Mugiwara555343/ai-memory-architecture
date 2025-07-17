from math import sqrt

while True:
    number = int(input("Please type in a number: "))
    if number < 0:
        print("Invalid number")
        
    
    elif number > 0:
        print(sqrt(number))
    
    
    elif number == 0:
        print("Exiting...")
        break

#below is the solution given above is the code i wrote
#the code given is more readable and understandable
#it also uses else statmenent for negative numbers

from math import sqrt

while True:

    number = int(input("Please type in a number: "))

    if number == 0:

        break

    if number > 0:

        print(sqrt(number))

    else:

        print("Invalid number")

        

print("Exiting...")