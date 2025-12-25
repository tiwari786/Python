# What is a Dictionary?
# A dictionary stores data in key : value pairs.

user = {"name": "Vipul", "age": 22, "city": "Jaipur"}


# Access dictionary values
print(user["name"])  # Vipul
print(user["age"])  # 22


# Add new key
user["email"] = "vipultiwari479@gmail.com"


# Update value
user["age"] = 21

# Remove key
user.pop("city")

# Check key exists
if "email" in user:
    print("user exists")


# Loop through dictionary ⭐
# Keys only
for key in user:
    print(key)


# Values only
for value in user.values():
    print(value)

# Key + Value
for key, value in user:
    print(key, value)


# Dictionary methods
user.keys()  # all keys
user.values()  # all values
user.items()  # key-value pairs


# Nested dictionary
user = {"id": 1, "name": "Vipul", "address": {"city": "Jaipur", "pincode": 302001}}

print(user["address"]["city"])


# List of dictionaries (API response style)
users = [{"id": 1, "name": "Vipul"}, {"id": 2, "name": "Aman"}]

for user in users:
    print(user["name"])


# List → ordered data
# Dictionary → named data
