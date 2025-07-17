year = int(input("Please type in a year: "))

leap_year = False

if year % 100 == 0:
    if year % 400 == 0:
        leap_year = True
elif year % 4 == 0:
    leap_year = True

if leap_year: 
    print("That year is a leap year.") 
else:
    print("That year is not a leap year.")

    