print("What is the weather forecast for tomorrow?")
Temp = int(input("Temperature: "))
rain = input("Will it rain (yes/no): ")

if Temp >= 20:
    print("Wear jeans and a T-shirt ")

if Temp <= 20:
    print("Wear jeans and a T-shirt ")
    print("I recommend a jumper as well ")

if Temp <= 10:
    print("Wear jeans and a T-shirt ")
    print("I recommend a jumper as well ")
    print("Take a jacket with you ")

if Temp <= 5:
    print("Wear jeans and a T-shirt ")
    print("I recommend a jumper as well ")
    print("Take a jacket with you ")
    print("Make it a warm coat, actually" \
    " I think gloves are in order")

if rain == "yes":
    print("Don't forget your umbrella!" )
