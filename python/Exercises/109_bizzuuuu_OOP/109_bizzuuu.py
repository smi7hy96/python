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
      "(Pick your own!)")
correct_input = False
while not correct_input:
    user_choice = input("Enter option 1,2 or 3 to play! \n")
    if game_1.check_if_number(user_choice):
        x = int(user_choice)
        if x == 1 or x == 2 or x ==3:
            correct_input = True
            game_1.type = x
            game_1.play()
        else:
            "Invalid Option. Try Again"

game_1.bizzzzuu_me()


print("Thanks for playing!")




