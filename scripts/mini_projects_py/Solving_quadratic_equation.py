from math import sqrt

a = int(input("Value of a: "))
b = int(input("Value of b: "))
c = int(input("Value of c: "))

root1 = (-b + sqrt(b**2 - 4*a*c)) / (2 * a)
root2 = (-b - sqrt(b**2 - 4*a*c)) / (2 * a)

print(f"The roots are {root1} and {root2}")