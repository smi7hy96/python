from generate_lists import *

names_list = load_file('names.txt')


def choice(question_string, choice_num):
    pos_num = False
    while not pos_num:  # will keep looping until valid number is entered
        user_number = input(question_string + "\n")  # ENTER THE MAXIMUM GROUP SIZE YOU WANT.
        # BEAR IN MIND IT WILL DISTRIBUTE GROUPS OUT AS EVENLY AS POSSIBLE
        if user_number.isnumeric():  # double checks input is a number
            user_number = int(user_number)
            if user_number > 0:  # and if its greater than 0 (cant have groups with nobody!)
                pos_num = True
                groups = generate_groups(choice_num, user_number, names_list)
            else:
                print("Sorry, number entered is less than 1")
        else:
            print("You didn't enter a number")
    return groups

def generate_groups(choice_num, user_num, names_list):
    groups = create_groups(choice_num, user_num, names_list)
    return groups



def run():
    valid_input = False
    while not valid_input:
        user_choice = input("How do you want to organise groups? \n 1) By Maximum Group Size \n 2) Total Number of Groups "
              "\n Enter number of choice \n")

        if user_choice.isnumeric():
            x = int(user_choice)
            if x == 1:
                valid_input = True
                groups = choice("Enter Max Group Size", x)
            elif x == 2:
                valid_input = True
                groups = choice("Enter Total Number of Groups", x)
            else:
                print("Invalid Choice")
        else:
            print("Didn't enter a number")
    return groups

