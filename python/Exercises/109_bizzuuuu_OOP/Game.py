class Game:

    def __init__(self, type, limit, cond_1, cond_2):  # initailise object instance, 4 params
        self.type = type  # set the parameters
        self.limit = limit
        self.cond_1 = cond_1
        self.cond_2 = cond_2

    def check_if_number(self, number):  # validation check to see if input is a number or not
        if number.isnumeric() and int(number) >= 1:  # is numeric checks that param is a number 0-9.
            # and also must be greater than 0
            return True  # return true to confirm it is a number
        else:
            print("You haven't typed in a valid number, please try again!")  # error message
            return False  # not a number, return false

    def get_params(self):  # function for setting the boundary numbers
        correct_input1 = False
        while not correct_input1:  # while loop to repeat picking numbers until two different numbers have been selected
            if self.cond_1 is None:  # check that the attribute of current object is empty
                param = input("Pick the lowest number: ")  # input number for the lower boundary
            else:  # if lower boundary already has a value, then ask for higher number
                param = input("Pick the highest number: ")
            if self.check_if_number(param) and int(param) != self.cond_1:  # check input with if number function
                # and also check that the number entered isn't equal to the value stored in the first boundary location
                correct_input1 = True
                return int(param)  # return the number
            else:
                print("Number is the same as first parameter - not allowed")  # error message

    def bizzzzuu_me(self):  # final function that prints all the numbers. doesn't need parameters
        bzu_list = []
        for x in range(int(self.limit)):  # for loop to repeat code a set number of times (the limit entered by user)
            y = x + 1  # loop count (x) starts at 0 instead of 1 so corrects that
            if y % self.cond_1 == 0 and y % self.cond_2 == 0:  # if divisible by both 3 and 5, add fizzbuzz to the list
                bzu_list.append("bizzzzuu")
            elif y % self.cond_1 == 0:  # if only divisible by 3, add fizz
                bzu_list.append("bizz")
            elif y % self.cond_2 == 0:  # if only divisible by 5, add buzz
                bzu_list.append("zzuu")
            else:
                bzu_list.append(y)  # if none of those, just add the number
        return bzu_list  # return the list

    def set_cond(self, cond_1, cond_2):
        self.cond_1 = cond_1  # set boundary 1
        self.cond_2 = cond_2  # set boundary 2

    def play(self):  # initial function that sets most of the attributes of the object
        correct_input = False
        while not correct_input:  # while loop to keep repeating until valid input has been entered
            user_number = input("Please enter the limit number now!\n")  # user enters max number
            if self.check_if_number(user_number):  # check if number
                self.limit = user_number  # if true, set number as limit in attribute
                correct_input = True  # return true, break while loop
                if self.type == 1:  # checking type (set in another method) there are only 3 types (1,2 or 3)
                    self.set_cond(3, 5)
                elif self.type == 2:  # same again but with different fixed numbers this time
                    self.set_cond(4, 9)
                else:  # if neither, then the game type has custom boundaries.
                    self.set_cond(self.get_params(), self.get_params())
