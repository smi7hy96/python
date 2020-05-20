import random
eng_57 = ['Nathan', 'Saskia', 'Samir', 'Ryan', 'Patrick', 'Marcus', 'Jonathan', 'Avraj', 'Ashraf', 'Delvin', 'Fahad',
          'Hussain', 'Mergim', 'Stefan']

pos_num = False
while not pos_num:
    max_group_size = input("Enter Max Group Size \n")
    if max_group_size.isnumeric():
        max_group_size = int(max_group_size)
        if max_group_size > 0:
            pos_num = True
        else:
            print("Sorry, number entered is less than 1")
    else:
        print("You didn't enter a number")

rand_num = random.randint(0, len(eng_57)-1)
range_num = -(len(eng_57) // -max_group_size)
groups = [[] for i in range(range_num)]

for x in range(max_group_size):
    for i in range(len(groups)):
        if len(eng_57) >= 1:
            rand_num = random.randint(0, len(eng_57) - 1)
            groups[i].append(eng_57[rand_num])
            eng_57.pop(rand_num)
        else:
            break

for x in range(len(groups)):
    print("GROUP " + str(x+1))
    print(groups[x])
