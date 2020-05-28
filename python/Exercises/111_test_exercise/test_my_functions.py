from my_functions import *

# SAY_HELLO() TEST
# Test with String
print("Testing function say_hello() with '  RyaN    ' --> 'Ryan'")
test_input = '  RyaN    '
expec_out = 'Hello Ryan'
print(say_hello(test_input) == expec_out)
# Test with Number
print("Testing function say_hello() with '50' --> 'Error'")
test_input = '50'
expec_out = 'Error'
print(say_hello(test_input) == expec_out)
# Test with String containing number
print("Testing function say_hello() with 'Salm0n' --> 'Error'")
test_input = 'Salm0n'
expec_out = 'Error'
print(say_hello(test_input) == expec_out)

# NUMBER_TIMES_TEN() TEST
# Test with fixed number
print("Testing function number_times_ten() with 5 --> 50")
test_input = '5'
expec_out = 50
print(number_times_ten(test_input) == expec_out)
# Test with String
print("Testing function number_times_ten() with 'Hi' --> 'Error'")
test_input = 'hello'
expec_out = 'Error'
print(number_times_ten(test_input) == expec_out)
