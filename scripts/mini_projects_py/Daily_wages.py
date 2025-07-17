wage = float(input("Hourly wage: "))
hours = float(input("Hours worked: "))
day = input("Day of the week: ")

result = wage * hours

if day == "Sunday":
    result = result * 2
 
print(f"Daily wages: {result}")
