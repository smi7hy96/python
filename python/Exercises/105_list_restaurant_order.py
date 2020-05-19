import time
# SIMPLEST - Restaurant Waiter Helper

# User Stories
#1
# AS a User I want to be able to see the menu in a formated way, so that I can order my meal.

#2
# AS a User I want to be able to order 3 times, and have my responses added to a list so they aren't forgotten

#3
# As a user, I want to have my order read back to me in formated way so I know what I ordered.

# DOD
# its own project on your laptop and Github
# be git tracked
# have 5 commits mininum!
# has documentation
# follows best practices

# starter code
# USER STORY 1
menu = ['Pizza', 'Burger', 'Enchiladas', 'Quesadillas', 'Just Cake :-)']
food_order = []
print("Here is today's Menu!!")
for (x, item) in enumerate(menu, start=1):
    print(x, item)
time.sleep(2)
# USER STORY 2
print("What would you like to order today? Use the numbers in the list to pick an item!")
item_1 = input("What will be the first item? \n")
food_order.append(item_1)
time.sleep(1)
item_2 = input("And the second? \n")
food_order.append(item_2)
time.sleep(1)
item_3 = input("And the final item? \n")
food_order.append(item_3)

# USER STORY 3
print("Your order is IN! Confirming...")
time.sleep(2)
for x in food_order:
    for i in range(len(menu)):
        if int(x) == (i+1):
           print(menu[i])

# I need to print each item from the list
# print(menu[0])
# before I print I need to make them all capitalized
# print everything
