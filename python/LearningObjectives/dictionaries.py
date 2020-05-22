# Dictionaries
# Definition and Syntax
# A dictionary is a data structure, like a list, but organised with keys and not an index
# They are organised with 'key' : 'value' pairs.
# This means you can search data using keys, rather than index

# Syntax
# {'key'  : 'value'}
# {'Zebra': 'Horse with stripes'}

# dictionary example
car_dict = {
  "brand": "Lamborghini",
  "model": "Aventador",
  "year": 2011
}

# printing dictionary
print(car_dict)
print(type(car_dict))

# getting one value out
print(car_dict['brand'])
print(car_dict['model'])

# re-assigning one value
car_dict['model'] = "Sesto Elemento"
car_dict['year'] = 2010
print(car_dict)

# new key-value pair
car_dict['price'] = "£2,000,000"
print(car_dict)
