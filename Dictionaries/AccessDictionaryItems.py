# Accessing Items.
# You can access the items of a dictionary by referring to its key name, inside square brackets.
# Get the value of the "model" key :
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict["model"]
print(x) # Mustang.

# There is also a method called get() that will give you the same result.
# Get the value of the "model" key :
x = thisdict.get("model")
print(x) # Mustang.

# Get Keys.
# The keys() method will return a list of all the keys in the dictionary.
# Get a list of the keys :
x = thisdict.keys()
print(x) # dict_keys(['brand', 'model', 'year']).

# Add a new item to the original dictionary, and see that the keys list gets updated as well :
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys()
print(x) # dict_keys(['brand', 'model', 'year']) (before the change).
car["color"] = "white"
print(x) # dict_keys(['brand', 'model', 'year', 'color']) (after the change).

# Get Values.
# The values() method will return a list of all the values in the dictionary.
# Get a list of the values :
x = thisdict.values()
print(x) # dict_values(['Ford', 'Mustang', 1964]).

# Make a change in the original dictionary, and see that the values list gets updated as well :
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x) # dict_values(['Ford', 'Mustang', 1964]) (before the change).
car["year"] = 2020
print(x) # dict_values(['Ford', 'Mustang', 2020]) (after the change).

# Add a new item to the original dictionary, and see that the values list gets updated as well :
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x) # dict_values(['Ford', 'Mustang', 1964]) (before the change).
car["color"] = "red"
print(x) # dict_values(['Ford', 'Mustang', 1964, 'red']) (after the change).

# Get Items.
# The items() method will return each item in a dictionary, as tuples in a list.
# Get a list of the key:value pairs :
x = thisdict.items()
print(x) # dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)]).

# Make a change in the original dictionary, and see that the items list gets updated as well :
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.items()
print(x) # dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)]) (before the change).
car["year"] = 2020
print(x) # dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2020)]) (after the change).

# Add a new item to the original dictionary, and see that the items list gets updated as well :
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.items()
print(x) # dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)]) (before the change).
car["color"] = "red"
print(x) # dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964), ('color', 'red')]) (after the change).

# Check if Key Exists.
# Check if "model" is present in the dictionary :
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")