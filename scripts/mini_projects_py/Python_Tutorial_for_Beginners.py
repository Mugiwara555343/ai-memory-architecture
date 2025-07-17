calc_of_units = 24
name_of_units = "hours"

#Functions for calculating days in hours
def days_of_units(num_of_days):
    
    #This checks if the number is greater than 0 return the calculation 
    if num_of_days > 0:
        return (f"{num_of_days} days are {num_of_days * calc_of_units} {name_of_units}")
    elif num_of_days == 0:
        return "You entered 0, please enter a positive number"
    else:
        return "You entered a negative value, so no conversion is possible!"

def validate_and_execute():
#This is another way to write a function instead of def var ()
#You add the var.isdigit()
#Below function is used to print a statment when a string is inputted 
#isdigit filter bad inputs that may ruin the program
    if user_input.isdigit():
        user_input_number = int(user_input)
        if user_input_number > 0:
            calc_value = days_of_units(user_input_number)
            print(calc_value) 
        elif user_input_number == 0:
            print("You entered 0, please enter a positive number")
    else:
        print("Your input is not a number")

user_input = input("Enter a number and I will convert it to hours \n")
validate_and_execute()




