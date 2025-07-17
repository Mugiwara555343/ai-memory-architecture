while True:
    password = input("Password: ")
    password_1 = input("Repeat password: ")
    
    if password == password_1:
        print("User account created!")
        break
    else:
        print("They do not match!")
        