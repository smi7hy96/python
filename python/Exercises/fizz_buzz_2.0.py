import time

print("Welcome to my Fizz Buzz Program!")
#time.sleep(2)
user_number = input("Please enter a number now!\n")

for x in range(int(user_number)):
    y = x+1
    if y % 3 == 0 and y % 5 == 0:
        print("fizzbuzz")
    elif y % 3 == 0:
        print("fizz")
    elif y % 5 == 0:
        print("buzz")
    else:
        print(y)
