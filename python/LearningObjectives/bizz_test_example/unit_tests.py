import unittest
from bizz_example import *  # import file for testing


class TestDivisibleNumber(unittest.TestCase):

    def test_check_if_digit_div_num(self):  # test_<method name> for clarity - could be called anything though
        self.assertEqual(check_if_digit_div_num(3, 3), True)  # assertequals checks that the output of the 1st arg == value of
        # second
        with self.assertRaises(TypeError):  # check for exceptions, for example with type errors (ie. wrong data type
            # inserted)
            check_if_digit_div_num('s', 's')  # run method with wrong data types - will not break because test is
            # checking the error exists


if __name__ == '__main___':
    unittest.main()
