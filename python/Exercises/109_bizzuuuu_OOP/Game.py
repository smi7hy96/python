class Game:

    def __init__(self, type, limit, cond_1, cond_2):
        self.type = type
        self.limit = limit
        self.cond_1 = cond_1
        self.cond_2 = cond_2

    def check_if_number(self, number):
        if number.isnumeric() and int(number) >= 1:
            return True
        else:
            print("You haven't typed in a valid number, please try again!")
            return False

    def get_params(self):
        correct_input1 = False
        while not correct_input1:
            if self.cond_1 is None:
                param = input("Pick a the lowest number: ")
            else:
                param = input("Pick a the highest number: ")
            if self.check_if_number(param) and int(param) != self.cond_1:
                correct_input1 = True
                return int(param)
            else:
                print("Number is the same as first parameter - not allowed")

    def bizzzzuu_me(self):
        for x in range(int(self.limit)):
            y = x + 1
            if y % self.cond_1 == 0 and y % self.cond_2 == 0:  # if divisible by both 3 and 5, print fizzbuzz
                print("bizzzzuu")
            elif y % self.cond_1 == 0:  # if only divisible by 3, print fizz
                print("bizz")
            elif y % self.cond_2 == 0:  # if only divisible by 5, print buzz
                print("zzuu")
            else:
                print(y)  # if none of those, just print the number

    def play(self):
        correct_input = False
        while not correct_input:
            user_number = input("Please enter the limit number now!\n")
            if self.check_if_number(user_number):
                self.limit = user_number
                correct_input = True
                if self.type == 1:
                    self.cond_1 = 3
                    self.cond_2 = 5
                elif self.type == 2:
                    self.cond_1 = 4
                    self.cond_2 = 9
                else:
                    self.cond_1 = self.get_params()
                    self.cond_2 = self.get_params()
