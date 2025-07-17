#While loop 
i = 1
while i <= 3:
    print("meow")
    i +=  1
#list loop, range statement is used for the loops amount
# for example [1, 2, 3] if you need 1 Mil write range(1000000)
for i in range(3):
    print("meow")

#another funny way is >>
print("meow\n" * 3)

#user input of how many meows are outputed 
while True:
    n = int(input("Whats n? "))
    if n < n:
        break 
#the under score is used as an indicator that a var is used to use the range statement
for _ in range(n):
    print("meow")

#now to print meow using a function
def main():
    meow(3)
#return is used to show value to user
#break is used to get out of loop
def get_number():
    while True:
        n = int(input("Whats n? "))
        if n < 0:
            break
    return n

def meow(n):
    for _ in range(n):
        print("meow")