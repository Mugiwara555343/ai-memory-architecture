attempts = 0  # Initialize the attempts counter

while True:
    pin = input("PIN: ")
    attempts += 1  # Increment the attempts counter

    if pin == "4321":
        if attempts == 1:
            print("Correct! It only took you one single attempt!")
        else:
            print(f"Correct! It took you {attempts} attempts")
        break  # Exit the loop when the correct PIN is entered
    else:
        print("Wrong")
