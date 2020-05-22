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


def check_if_number(number):
    if number.isnumeric() and int(number) >= 1:
        return True
    else:
        print("You haven't typed in a valid number, please try again!")
        return False


def bizzzzuu_me(limit, param1, param2):
    for x in range(int(limit)):
        y = x + 1
        if y % param1 == 0 and y % param2 == 0:  # if divisible by both 3 and 5, print fizzbuzz
            print("bizzzzuu")
        elif y % param1 == 0:  # if only divisible by 3, print fizz
            print("bizz")
        elif y % param2 == 0:  # if only divisible by 5, print buzz
            print("zzuu")
        else:
            print(y)  # if none of those, just print the number


def get_params(position, previous_param):
    correct_input1 = False
    while not correct_input1:
        param = input("Pick a number for the " + position + " number: ")
        if check_if_number(param) and int(param) != previous_param:
            correct_input1 = True
            return int(param)
        else:
            print("Number is the same as first parameter - not allowed")


def play(choice):
    correct_input = False
    while not correct_input:
        user_number = input("Please enter the limit number now!\n")
        if check_if_number(user_number):
            correct_input = True
            if choice == 1:
                bizzzzuu_me(user_number, 3, 5)
            elif choice == 2:
                bizzzzuu_me(user_number, 4, 9)
            else:
                param1 = get_params('lowest', 0)
                param2 = get_params('highest', param1)
                bizzzzuu_me(user_number, param1, param2)


print("WELCOME! How would you like to play BIZZZZUU?: \n 1) Standard (3 and 5) \n 2) Bigger (4 and 9) \n 3) Custom "
      "(Pick your own!)")
correct_input = False
while not correct_input:
    user_choice = input("Enter option 1,2 or 3 to play! \n")
    if check_if_number(user_choice):
        x = int(user_choice)
        if x == 1 or x == 2 or x ==3:
            correct_input = True
            play(x)
        else:
            "Invalid Option. Try Again"




print("Thanks for playing!")




