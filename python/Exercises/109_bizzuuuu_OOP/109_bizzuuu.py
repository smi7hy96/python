# Write a bizz and zzuu game ##project

# as a user I should be able prompted for a number, as the program will print all the number up to and inclusing said number while following the constraints / specs. (bizz and buzz for multiples or 3 and 5)

# As a user I should be able to keep giving the program different numbers and it will calculate appropriately until you use the key word: 'penpinapplespen'


# write a program that take a number
# prints back each individual number, but
    # if it is a multiple of 3 it returns bizz
    # if a multiple of 5 it return zzuu
    # if a multiple of 3 and 5 it return bizzzzuu


#  EXTRA:
#  Make it functional
#  make it so I can it so it can work with 4 and 9 insted of 3 and 5.
    #      make it so it can work with any number!
from Game import *

game_1 = Game(None, None, None, None)

print("WELCOME! How would you like to play BIZZZZUU?: \n 1) Standard (3 and 5) \n 2) Bigger (4 and 9) \n 3) Custom "
      "(Pick your own!)")  # welcome message
correct_input = False
while not correct_input:  # check input while loop. keeps repeating until condition true
    user_choice = input("Enter option 1,2 or 3 to play! \n")  # ask for input
    if game_1.check_if_number(user_choice):  # check if input is actually a number
        x = int(user_choice)  # now confirmed, convert input type to integer
        if x == 1 or x == 2 or x ==3:  # check that number entered is one of the 3 expected inputs
            correct_input = True  # if it is, set true and break while loop
            game_1.type = x  # set the object type as the user input
            game_1.play()  # execute function play, in Game.py
        else:
            "Invalid Option. Try Again"  # error message

print(game_1.bizzzzuu_me())  # prints the list returned from the method,can print every item on a separately if needed
# (see commented code below)
# bzu_list = game_1.bizzzzuu_me()  # for clarity, store returned list as new variable
# for item in bzu_list:  # loop through each item in list
#     print(item)  # print item


print("Thanks for playing!")  # Thanks you message




