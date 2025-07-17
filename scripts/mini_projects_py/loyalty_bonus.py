# Fix the program
points = int(input("How many points are on your card? "))
result = points * 1.1

if points < 100:
    print("Your bonus is 10 %")

if points >= 100:
    result = points * 1.15
    print("Your bonus is 15 %")

print(f"You now have {result} points")