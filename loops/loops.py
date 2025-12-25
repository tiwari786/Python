# What is a Loop?
# A loop runs the same code again and again until a condition ends

# 1.for loop (Used when you know how many times to run or you’re looping over data)
for i in range(5):
    print(i)

# Output:
# 0
# 1
# 2
# 3
# 4

# Loop through a list
colors = ["red", "blue", "green"]
for color in colors:
    print(color)

# Output:
# red
# blue
# green

# Loop through numbers (range)
for i in range(1, 6):  # range(start, end) → end is not included in output.
    print(i)

# Output:
# 1
# 2
# 3
# 4
# 5

# Loop through dictionary
user = {"name": "Vipul", "age": 22, "city": "Jaipur"}

for key, value in user.items():  # View of (key, value) pairs
    print(key, value)

# Method 	Returns          	         Use Case

# .keys()	View of all keys	         When you only need the identifiers.
# .values()	View of all values	         When you only need the data, not the keys.
# .items()	View of (key, value) pairs	 When you need both for processing or display.


# 2.while loop (Used when you don’t know how many times the loop will run)
count = 1

while count <= 5:
    print(count)
    count += 1

# Always update condition, otherwise infinite loop

# Output:
# 1
# 2
# 3
# 4
# 5


# break (stop loop)
for i in range(1, 10):
    if i == 5:
        break
    print(i)

# Stops loop at 4
# Output:
# 1
# 2
# 3
# 4

# continue (skip current step)
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# Skips 3
# Output:
# 1
# 2
# 4
# 5


# Backend-style examples
# Example 1: Loop through users

users = [
    {"name": "Vipul", "role": "admin"},
    {"name": "Aman", "role": "user"},
]

for user in users:
    print(user["name"])


# Example 2: Find admin user
for user in users:
    if user["role"] == "admin":
        print("Admin found")
        break

# Example 3: Count active users
users = [{"active": True}, {"active": False}, {"active": True}]

count = 0
for user in users:
    if user["active"]:
        count += 1  

print(count)