import random

number_to_guess = random.randint(1, 200)
attempts = 0

while True:
    guess = int(input("Guess the number (1, 200): "))
    attempts += 1

    if guess == number_to_guess:
        print(f"Congrats! You guessed the number in {attempts} attempts")
        break
    elif guess < number_to_guess:
        
        print("Guess a higher number")
    else:
        print("Guess a lower number")