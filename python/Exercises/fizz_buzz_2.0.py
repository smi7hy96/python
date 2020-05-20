import time  # imported so i can use sleep command

print("Welcome to my Fizz Buzz Program!")  # welcome message
time.sleep(2)  # used throughout - delays following code execution by number of seconds in the ()

kill_code = False  # boolean to indicate whether key phrase has been entered
failure_count = 0  # count to control fun add on to insult user's intelligence
while not kill_code:  # while kill code is false always repeat following code
    time.sleep(.75)
    # SEGMENT 1 -- depending on number of failures from user changes the printed message asking for user input
    if failure_count == 0:
        user_number = input("Please enter a number (or kill code) now!\n")
    elif failure_count == 1:
        user_number = input("Enter number or kill code this time!\n")
    elif failure_count == 2:
        user_number = input("3rd time lucky?\n")
    elif failure_count == 3:
        user_number = input("Getting tired of asking you now\n")
    else:
        user_number = input("Again.\n")
    # SEGMENT 1 END
    if user_number.isnumeric():  # Checks if the user has entered a number
        # If the user has already failed numerous times, the program mocks them when they get it right.
        if failure_count >= 3:
            print("FINALLY")
            time.sleep(1.25)
            # SEGMENT 2 -- loops through a set number of times depending on number entered by user
        for x in range(int(user_number)):
            y = x + 1
            if y % 3 == 0 and y % 5 == 0:  # if divisible by both 3 and 5, print fizzbuzz
                print("fizzbuzz")
            elif y % 3 == 0:  # if only divisible by 3, print fizz
                print("fizz")
            elif y % 5 == 0:  # if only divisible by 5, print buzz
                print("buzz")
            else:
                print(y)  # if none of those, just print the number
        time.sleep(1)
        print("That was fun!")
        # SEGMENT 2 END
        # SEGMENT 3 -- user input was not a number but an ordinary string
    else:
        # SEGMENT 3.1 -- kill code
        if user_number.lower() == "killme":  # Check if string equals password to kill program
            kill_code = True  # change boolean to true so that this becomes last iteration
            if failure_count >= 3:  # if failed numerous times, mock the user
                print("About time! Please don't come back")
            else:  # if not failed, tell the user that you have killed the program
                for char in "...":
                    print(char, end="")
                    time.sleep(.5)
                print("\nAs you wish")
        # END SEGMENT 3.1
        # SEGMENT 3.2 -- not kill code. user has failed this time
        else:
            time.sleep(1)
            if failure_count == 0:  # check how many times user has already failed using the count
                print("You haven't typed in kill code or a number, please try again!")
            elif failure_count == 1:
                print("Once again, wrong!")
            elif failure_count == 2:
                print("Come on really?")
            elif failure_count == 3:  # messages get steadily more degrading before losing all patience
                print("I Give up")
            else:
                print("Nope")
            failure_count += 1  # increment count each time
