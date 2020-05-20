import random
eng_57 = ['Nathan', 'Saskia', 'Samir', 'Ryan', 'Patrick', 'Marcus', 'Jonathan', 'Avraj', 'Ashraf', 'Delvin', 'Fahad',
          'Hussain', 'Mergim', 'Stefan']  # names in the class

pos_num = False
while not pos_num:  # will keep looping until valid number is entered
    max_group_size = input("Enter Max Group Size \n")  # ENTER THE MAXIMUM GROUP SIZE YOU WANT.
    # BEAR IN MIND IT WILL DISTRIBUTE GROUPS OUT AS EVENLY AS POSSIBLE
    if max_group_size.isnumeric():  # double checks input is a number
        max_group_size = int(max_group_size)
        if max_group_size > 0:  # and if its greater than 0 (cant have groups with nobody!)
            pos_num = True
        else:
            print("Sorry, number entered is less than 1")
    else:
        print("You didn't enter a number")

range_num = -(len(eng_57) // -max_group_size)  # generates how many groups will be created
# based on length of list and user input
groups = [[] for i in range(range_num)]  # creates a new list that will contain more lists!
# number of lists in parent list is determined by range_num

for x in range(max_group_size):  # loop through set number of times (max number of people)
    for i in range(len(groups)):  # then loop through the length of the parent list
        if len(eng_57) >= 1:  # double check the original class list is not empty!
            rand_num = random.randint(0, len(eng_57) - 1)
            # ^^ generate random number between 0 and length of list (ie. an index)
            groups[i].append(eng_57[rand_num])  # get the person from the class list (retrieved from random position)
            # and then add them to one of the lists inside the parent list.
            # (which list is determined by which iteration in loop it is in.
            eng_57.pop(rand_num)  # remove the person added from the class list so they cannot be added again to
            # another group
        else:
            break  # if the class list is now empty - stop the loop process - any other iterations are redundant

for x in range(len(groups)):  # loop through the parent list
    print("GROUP " + str(x+1))
    print(groups[x])  # print out the child lists containing the group members
