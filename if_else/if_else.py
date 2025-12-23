# What is if-else in Python?
# It helps you make decisions based on conditions

# Syntax
# if condition:
# code runs if condition is true
# else:
# code runs if condition is false

# Python uses indentation (spaces), not {} like JS


# Example
age = 20

if age >= 18:
    print("You can vote")
else:
    print("You are underage")


# if – elif – else (Used when there are multiple conditions)
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
else:
    print("Grade C")


# Comparison operators (Used inside conditions:) (==, !=, >, <, >=, <=)
a = 10
b = 5

if a > b:
    print("a is greater")

# Logical operators (Used to combine conditions) (and, or, not)

# and
age = 22
is_logged_in = True

if age >= 18 and is_logged_in:
    print("Access granted")

# or
is_admin = False
is_editor = True

if is_admin or is_editor:
    print("You can edit")

# not
is_blocked = False

if not is_blocked:
    print("User is active")


# Backend-style example
email = "vipultiwari479@gmail.com"
password = "123"

if email == "vipul@gmail.com" and password == "1234":
    print("Login successful")
else:
    print("Invalid credentials")


# Using if-else with dictionary
user = {"name": "Vipul", "is_admin": False}

if user["is_admin"]:
    print("Admin access")
else:
    print("User access")
