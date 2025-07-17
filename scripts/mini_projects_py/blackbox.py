print("What is the weather forecast for tomorrow?")

temperature = int(input("Temperature: "))

rain = input("Will it rain (yes/no): ")

print("Wear jeans and a T-shirt")

if temperature < 21:

    print("I recommend a jumper as well")

if temperature < 11:

    print("Take a jacket with you")

if temperature < 6:

    print("Make it a warm coat, actually")

    print("I think gloves are in order")

if rain == "yes":

    print("Don't forget your umbrella!")