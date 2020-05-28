# FUNCTIONS


def contains_number(in_string):  # Function to check if string contains a digit within it
    for char in in_string:  # Loop through string
        if char.isdigit():  # check if character is a digit or not
            return True
    return False


def say_hello(name):  # return 'hello + formatted name'
    if not contains_number(name):  # check if arg contains a number using function 'contains_number'
        config_name = name.title().strip()  # format the name by capitalising each word and remove extra spaces
        return f'Hello {config_name}'  # return formatted string
    else:
        return "Error"  # return an error


def number_times_ten(input_num):  # function for multiplying number by 10
    if input_num.isnumeric():  # check that whole string is only numbers
        return int(input_num) * 10  # convert string to integer and multiply by 10. return result
    else:
        return "Error"  # return an error
