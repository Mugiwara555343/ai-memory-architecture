letter_1 = input("1st letter: ")
letter_2 = input("2nd letter: ")
letter_3 = input("3rd letter: ")

if letter_1 < letter_2 < letter_3 or letter_1 > letter_2 > letter_3:
    middle = letter_2

elif letter_2 < letter_1 < letter_3 or letter_2 > letter_1 > letter_3:
    middle = letter_1

else: 
    middle = letter_3

print(f"The letter in the middle is {middle}")