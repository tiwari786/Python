# What is a Variable in Python?

# A variable is like a container that stores data.
# You don’t need to define the type in Python.
# Python automatically understands it.

name = "vipul"
age = 21


# Data Types in Python

# 1.integer ((int)Used for whole numbers)
age = 21
count = 5

# 2.Float ((float) Used for decimal numbers)
price = 199.99
rating = 4.5

# 3.String ((str)Used for text. Always inside quotes)
name = "Vipul"
city = "Jaipur"

# 4.Boolean ((bool)Used for true/false conditions)
is_logged_in = True
is_admin = False

# 5.List ((list)Used to store multiple values in one variable, Ordered and changeable)
colors = ["red", "blue", "green"]
numbers = [1, 2, 3, 4]

# access values form list
print(colors[0])  # red


# 6.Tuple ((tuple)Same as list but cannot be changed)
roles = ("admin", "user")


# 7.Dictionary((dict)Stores data as key : value pairs (like JSON).)
user = {"name": "Vipul", "age": 22, "city": "Jaipur"}
# access value from dict
print(user["name"])  # Vipul
# This is exactly how backend sends data to frontend


# 8.Set ((set)Stores unique values only)
ids = {1, 2, 3, 3}
print(ids)  # {1, 2, 3}


# check type of variables
x = 10
print(type(x))  ## <class 'int'>


# Real backend-style example
user = {"id": 1, "name": "Vipul", "email": "vipul@gmail.com", "is_active": True}
print(user["name"])  # Vipul


# JS Object = Python dictionary
# JS Array = Python list
# true/false = True/False
