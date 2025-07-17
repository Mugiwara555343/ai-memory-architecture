Temp = int(input("Please type in a temperature (F): "))

result = (Temp - 32) * 5 / 9

print(f"{Temp} degrees Fahrenheit equals {result} degrees Celsius")

if result <= -1:
    print("Brr! It's cold in here!")
