# FUNCTIONS


def say_hello(name):
    if not name.isnumeric():
        config_name = name.title().strip()
        return (f'Hello {config_name}')
    else:
        return "Error"


def number_times_ten(input):
    if input.isnumeric():
        return int(input) * 10
    else:
        return "Error"
