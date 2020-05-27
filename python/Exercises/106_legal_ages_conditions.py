age = 19
driver_license = True


# - You can vote and drive
# - You can vote
# - You can driver
# - you can't legally drink but your mates/uncles might have your back (bigger 16)
# - Your too young, go back to school!
def age_response(new_age):
    if new_age >= 18:
        print("You can drink, drive and vote (BUT NOT AT THE SAME TIME PLEASE!)")
    elif new_age == 17:
        print("You can vote and drive but you can't drink sorry!")
    elif new_age == 16:
        print("You can vote now but got to wait before you can do anything else")
    else:
        print("You're too young! Go back to school!")

 # as a user I should be able to keep being prompted for input until I say 'exit'
exit_boolean = False
while not exit_boolean:
    user_input = input("How old are you? (Type 'exit' when you want to quit) \n").lower()

    if user_input.isnumeric():
        age_response(int(user_input))
    else:
        if user_input == "exit":
            exit_boolean = True
print("EXIT COMPLETE")
