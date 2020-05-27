# Magic number game!
# I want you to use operators
# equate something
# As a user, I want to be able to guess a number and know if i got it correct or not, so that I can know if I won or not.
import random

# We should define/assign number to a variable called magic_number
magic_number = random.randint(1, 10)

# I need to ask user for input
user_guess = int(input("Guess which number is the magic number! \n"))

# I need to check if this input matches a magic_number
if user_guess == magic_number:
    print("YOU GUESSED RIGHT! CONGRATULATIONS")
else:
    print(f'Ah. Wrong answer, better luck next time! (Answer was {magic_number})')

# I need to let the user know if the response was right or not
#self five

