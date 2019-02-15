# Basal Metabolic Rate Calculator for Males

weight = int(input("Enter your weight in kg:\n")) # convert user input into an int
height = int(input("Enter your height in cm:\n"))
age = int(input("Enter your age:\n"))
isMale = str(input("Are you male? (y/n)"))

if isMale == "y":
    isMale = True
elif isMale == "n":
    isMale = False
else:
    print("Error")
    quit()

if isMale:
    bmr = 66.5 + (13.75 * weight) + (5 * height) - (6.755 * age)
else:
    bmr = 655.1 + (9.6 * weight) + (1.8 * height) - (4.7 * age)

bmr = round(bmr)
print(bmr)
