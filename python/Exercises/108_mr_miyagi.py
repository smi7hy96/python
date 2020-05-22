# Mr Miyagi trainee

# make a Mr Miyagi virtual assistant

# as a user I should be able to speak with Mr Miyagi and get appropriate response s as I go
print("MR MIYAGI VIRTUAL ASSISTANT \n")

name = input("Enter your name \n")
print("Say Something Below " + name + ":")
# Ask for user input and depending on the response, Mr Miyagi will respond.
end_code = False

#  make it run continuously
while not end_code:
    response_count = 0
    # prompt user for input
    user_input = input("[Mr Miyagi] Yes???\n" + "[" + name + "] ").lower()
    # Make it so you keep playing until we say: 'Sensei, I am at peace'
    # --> 'Sometimes, what heart know, head forget'
    if user_input == "sensei, i am at peace":
        end_code = True
        print("[Mr Miyagi] Sometimes, what heart know, head forget")
    else:
        # every statement/question must start with Sensei, otherwise:
        # --> 'You are smart, but not wise - address me as Sensei please'
        if not user_input.capitalize().startswith("Sensei"):
            print("[Mr Miyagi] You are smart, but not wise - address me as Sensei please")
            response_count += 1
            # every time you ask a question --> Mr. Miyagi responde with
            # --> 'questions are wise, but for now. Wax on, and Wax off!'
        if user_input.strip().endswith('?'):
            print("[Mr Miyagi] Questions are wise, but for now. Wax onm Wax off!")
            response_count += 1
            # every time you mention 'block' or 'blocking' --> Mr. Miyagi responde with
            # --> 'Remember, best block, not to be there..'
        if ("block") in user_input or ("blocking") in user_input:
            print("[Mr Miyagi] Remember, best block, not to be there..")
            response_count += 1
            # anything else you say:
            # --> 'do not lose focus. Wax on. Wax off.'
        if response_count == 0:
            print("[Mr Miyagi] Do not lose focus. Wax on. Wax off.")
# Evaluate each input and print the appropriate responses


#  EXTRA:

#  consider best practices of functions - make this functional