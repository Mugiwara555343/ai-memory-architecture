def findLeapYears(n):
    year = 2024
    count = 0
    while count < n:
        if (year % 4) == 0:
            if (year % 100) == 0:
                if (year % 400) == 0:
                    print(year)
                    count += 1
            else:
                print(year)
                count += 1
        year += 1

# test the function
findLeapYears(int(input('Enter the number of leap years you want to display: ')))