points = int(input("How many points [0-100]: "))

#Below is the list of points with correlating grades

if points >= 0 and points <= 49:
    print("Grade: fail")
elif points >= 50 and points <= 59:
    print("Grade:", 1)
elif points >= 60 and points <= 69:
    print("Grade:", 2)
elif points >= 70 and points <= 79:
    print("Grade:", 3)
elif points >= 80 and points <= 89:
    print("Grade:", 4)
elif points >= 90 and points <= 100:
    print("Grade:", 5)

else:
    print("Grade: impossible! ")

points = int(input("How many points [0-100]: "))

 

if points < 0 or points > 100:

    grade = "impossible!"

elif points < 50:

    grade = "fail"

elif points < 60:

    grade = "1"

elif points < 70:

    grade = "2"

elif points < 80:

    grade = "3"

elif points < 90:

    grade = "4"

else:

    grade = "5"

 

print(f"Grade: {grade}")

 

