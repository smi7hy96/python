import random
eng_57 = ['Nathan', 'Saskia', 'Samir', 'Ryan', 'Patrick', 'Marcus', 'Jonathan', 'Avraj', 'Ashraf', 'Delvin', 'Fahad',
          'Hussain', 'Mergim', 'Stefan']


max_group_size = int(input("Enter Max Group Size \n"))

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
