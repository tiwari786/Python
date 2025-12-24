# What is a Function?
# A function is a block of code that does one job and can be reused

# Syntax:

# def function_name():
# code


# basic function
def greet():
    print("Hello world!!")


greet()  # Hello world!!


# Function with parameters
# Parameters are values you pass to a function


def add(a, b):
    print(a + b)


add(10, 20)  # 30


# with return
def add(a, b):
    return a + b


print(add(10, 20))
# Backend APIs always use return


# Function with condition
def check_age(age):
    if age >= 18:
        return "Adult"
    else:
        return "Minor"


print(check_age(22))


# Default parameters
def greet(name="User"):
    return f"Helloo {name}"  # Python's f-strings work almost exactly like template literals   	f"Hello {name}" = `Hello ${name}`


print(greet())  # Helloo User
print(greet("Vipul"))  # Helloo Vipul


# Functions with list
def total_marks(marks):
    total = 0
    for m in marks:
        total += m
    return total


print(total_marks([10, 80, 70]))  # 160


# Function with dictionary
def get_user_name(user):
    return user["name"]


user = {"name": "Vipul", "age": 22}
print(get_user_name(user))  # Vipul


# Real backend-style example (Login check)
def login(email, password):
    if email == "vipul@gmail.com" and password == "1234":
        return {"success": True, "message": "Login successful"}
    else:
        return {"success": False, "message": "Invalid credentials"}


response = login("vipul@gmail.com", "1234")
print(response)