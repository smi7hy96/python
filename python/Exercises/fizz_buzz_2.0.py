import time

print("Welcome to my Fizz Buzz Program!")
time.sleep(2)

kill_code = False
failure_count = 0
while not kill_code:
    time.sleep(.75)
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
    if user_number.isnumeric():
        if failure_count >= 3:
            print("FINALLY")
            time.sleep(1.25)
        for x in range(int(user_number)):
            y = x + 1
            if y % 3 == 0 and y % 5 == 0:
                print("fizzbuzz")
            elif y % 3 == 0:
                print("fizz")
            elif y % 5 == 0:
                print("buzz")
            else:
                print(y)
        time.sleep(1)
        print("That was fun!")
    else:
        if user_number.lower() == "killme":
            kill_code = True
            if failure_count >= 3:
                print("About time! Please don't come back")
            else:
                for char in "...":
                    print(char, end="")
                    time.sleep(.5)
                print("\nAs you wish")
        else:
            time.sleep(1)
            if failure_count == 0:
                print("You haven't typed in kill code or a number, please try again!")
            elif failure_count == 1:
                print("Once again, wrong!")
            elif failure_count == 2:
                print("Come on really?")
            elif failure_count == 3:
                print("I Give up")
            else:
                print("Nope")
            failure_count += 1
