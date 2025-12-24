# List (list)
# Used to store multiple values in one variable.
# - Ordered
# - Changeable
# - Allows duplicates


# Create a list
fruits = ["apple", "banana", "mango"]
numbers = [10, 20, 30]


# Access list items
print(fruits[2])  # mango
print(fruits[-2])  # banana
print(fruits[-1])  # mango


# Change list value
fruits[1] = "Orange"
print(fruits)


# Add items
fruits.append("Graps")  # add at end
fruits.insert(1, "kiwi")  # add at index


# Remove items
fruits.remove("apple")
fruits.pop()  # removes last
fruits.pop(0)  # removes by index


# Loop through list
for number in numbers:
    print(number)

# Output:
# 10
# 20
# 30


# Common list methods
numbers.append(5)
numbers.sort()  # Reorganizes the items in the list into ascending order (smallest to largest)
numbers.reverse()  # Flips the order of the list entirely


# Backend-style list example
users = [
    {"name": "Vipul", "role": "admin"},
    {"name": "Aman", "role": "user"}
]

for user in users:
    print(user["name"])