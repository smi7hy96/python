# Define the following variables - DEFINED ON LINES 18-22
# name, last_name, age, eye_color, hair_color
# name = ''
# last_name = ''
# eye_color = ''
# hair_color = ''
# age = ''
# Prompt user for input and Re-assign these - DEFINED ON LINES 24-28
# Print them back to the user as conversation - DEFINE ON LINE 29
# Example: 'Hello Jack! Welcome, your age is 26, your eyes are green and your hair color is black.
# Extra Section 2 - Calculate in what year was the person born? and respond back. - DEFINED ON LINE 33-34
# print something like: 'You said you we're 28 hence you were born in 1991!'
# Extra - Cast your input - DEFINE ON LINE 30 & 34 --- str()
#

import datetime # Used to retrieve date

# create variables
name = "Ryan"
last_name = "Smith"
eye_color = "blue-grey"
hair_color = "brown"
age = 23

# overwrite variables with user input
name = input("What is your first name? \n")
last_name = input("And your surname? \n")
age = int(input("How old are you? \n"))
eye_color = input("What colour are your eyes? \n")
hair_color = input("What colour is your hair? \n")
# print variables
print("Hello, " + name + " " + last_name +
      "! You are " + str(age) + " Years Old. " +
      "Your eyes are " + eye_color + " and your hair is " + hair_color)

curr_date = datetime.datetime.now()  # retrieve current date
# calculate year born using current year and age
print("I guess that you were born in " + str(curr_date.year - age))
