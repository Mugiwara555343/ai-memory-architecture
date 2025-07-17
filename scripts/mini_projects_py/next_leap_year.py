# Step 1: Ask the user for a year
year = int(input("Year: "))

# Step 2: Check if it's a leap year
is_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Step 3: Find the next leap year
while not is_leap_year:
    year += 1
    is_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Step 4: Print the next leap year
print(f"The next leap year after {year - 1} is {year}")
