# STRINGS

# QUOTATIONS

# single_quotes = ' Look! Single Quotes'  # cannot use apostrophe as it ends string
# print(single_quotes)
#
# double_quotes = " It's Double quotes"  # can use apostrophe without issue
# print(double_quotes)
#
# single_apost = ' I said \'Wow!\''  # backslash escapes string to use apostrophe within apostrophe. Not nice looking
# print(single_apost)
#
# quote_in_quote = 'I said "Wow!"'  # use double quotes within instead. But doesn't look right in output
# print(quote_in_quote)
#

# SLICING

# Hw = "Hello World!"
# print(Hw[:5])  # Selecting certain characters from a string
# print(len(Hw))  # print length of whole string
#
# STRIP
#
# white_space = "lot's of space at the end               "
# print(len(white_space))  # print length of string which includes spaces at end
# print(len(white_space.strip()))  # .strip() removes spaces at beginning & end of string

# COUNT

# example_text = "some text here"
# print(example_text.count("e"))  # count number of times matching letter (or string) appears in variable

# LOWER CASE/ UPPER CASE
# print(example_text.lower())
# print(example_text.upper())
# print(example_text.capitalize())  # capitalises first character of string
#
# # REPLACE
# print(example_text.replace("text here", "BODY"))  # replace certain characters with others -
# if it doesnt exist it wont replace anything

#  CONCATENATION AND CASTING

# x = 2
# y = 10.5
# z = "it's me"
#
# print(z + " " + str(y) + " " + str(x) + " " + str(x+y))

# QUICK TASK
# x1 = "100"
# # type
# print(type(x1))
# # change to int
# print(type(int(x1)))
# # change to float
# print(type(float(x1)))

# BOOLEAN OPERATORS - TRUE & FALSE

# a = True
# b = False
# c = 2
# d = 1
#
# print(c == d)  # is c equal to d
# print(c != d)  # is c not equal to d
# print(c > d)  # is c greater than d
# print(c < d)  # is c less than d

# greeting = "Hello World!"
#
# print(greeting.startswith("H"))  # Check if it starts with 'H'
# print(greeting.endswith("!"))  # Check if it ends with '!'

