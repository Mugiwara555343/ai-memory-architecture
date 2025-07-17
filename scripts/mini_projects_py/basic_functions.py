#All paramaters defined by the function example "last_name" are required
def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name} ")
    print("Welcome aboard")

# or it will give an error
greet("Mauricio", "Storm")
greet("John", "Cena") 

def greet(name):
    print(f"Hi {name}")

def get_greeting(name):
    return(f"Hi {name}")

#this function pretty much multiplys all the number in line 9 

def multiply (*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total

print(multiply(2, 3, 4, 5))