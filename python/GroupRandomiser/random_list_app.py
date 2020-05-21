from user_choices import *

print("RANDOMISE LIST APP \n")

groups = run()

for i in range(len(groups)):  # loop through the parent list
    print("GROUP " + str(i+1))
    print(groups[i])  # print out the child lists containing the group members