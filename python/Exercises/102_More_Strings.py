import datetime
# Practice strings
# Welcome to Sparta - exercise
# Version 1 specs - with concatenation
# define a variable name, and assign a string
user_name = "Anne"
# prompt the user for input and ask the user for his/her name
# re assign the original variable this this input
user_name = input("What is your name? \n")
# use concatenation to print a welcome message and use methods to format the name/input (remove white spaces)
print("Welcome " + user_name.strip())
# Version 2 - with interpolation
# ask the user for a first name, save it in a variable
first_name = input("Please enter your first name \n")
# ask the user for a last name, save it in a variable
last_name = input("Please enter your last name \n")
# use interpolation to print the message
print(f"Hello {first_name} {last_name}! Welcome!!")
# Calculate year of birth
# gather details on age and name
age = int(input("How old are you? \n"))
curr_date = datetime.datetime.now()
year_Born = str(curr_date.year - age)
# print something like
# OMG <person>, you are <age> years old so you were born in <year>
print(f"OMG {first_name} {last_name}, you are {age} so you were born in {year_Born}!")