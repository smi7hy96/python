from bizz_example import check_if_digit_div_num

# TEST FOR DIGIT 3 DIV 3
print("testing for 3 divided by 3, should be true")
ex_num = 3
ex_div = 3
exp_output = True
print(check_if_digit_div_num(ex_num, ex_div) == exp_output)
# TEST FOR DIGIT 3 DIV 3
print("testing for 4 divided by 3, should be false")
ex_num = 4
ex_div = 3
exp_output = False
print(check_if_digit_div_num(ex_num, ex_div) == exp_output)
# TEST FOR DIGIT 5 DIV 5
print("testing for 3 divided by 3, should be true")
ex_num = 5
ex_div = 5
exp_output = True
print(check_if_digit_div_num(ex_num, ex_div) == exp_output)
# TEST FOR DIGIT 3 DIV 3
print("testing for 6 divided by 5, should be false")
ex_num = 6
ex_div = 5
exp_output = False
print(check_if_digit_div_num(ex_num, ex_div) == exp_output)
# TEST FOR DIGIT 15 DIV 3
print("testing for 15 divided by 3, should be true")
ex_num = 15
ex_div = 3
exp_output = True
print(check_if_digit_div_num(ex_num, ex_div) == exp_output)
# TEST FOR DIGIT 3 DIV 3
print("testing for 15 divided by 5, should be true")
ex_num = 15
ex_div = 5
exp_output = True
print(check_if_digit_div_num(ex_num, ex_div) == exp_output)
