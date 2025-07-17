num_1 = int(input("Number 1: "))
num_2 = int(input("Number 2: "))
opp = input("Operation: ")

if opp == "add":
    result = num_1 + num_2
    print(f"{num_1} + {num_2} = {result}")
if opp == "multiply":
    result_1 = num_1 * num_2
    print(f"{num_1} * {num_2} = {result_1}")
if opp == "subtract":
    result_2 = num_1 - num_2
    print(f"{num_1} - {num_2} = {result_2}")
