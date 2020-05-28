# FUNCTIONS


def contains_number(in_string):
    for char in in_string:
        if char.isdigit():
            return True
    return False


def say_hello(name):
    if not contains_number(name):
        config_name = name.title().strip()
        return (f'Hello {config_name}')
    else:
        return "Error"


def number_times_ten(input):
    if input.isnumeric():
        return int(input) * 10
    else:
        return "Error"
