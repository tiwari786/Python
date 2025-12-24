# Set (set)
# Stores unique values only.
# - No duplicates
# - No index
# - Unordered


# Create set
ids = {1, 2, 3, 3, 4}
print(ids)  # {1, 2, 3, 4}


# Add & remove
ids.add(5)  # its add 5 at the end
ids.remove(2)  # its remove 2 from ids


# Check value exists
if 3 in ids:
    print("Exists")


# Set use-case (backend)
# Remove duplicate emails:
emails = ["a@gmail.com", "b@gmail.com", "a@gmail.com"]

unique_emails = set(emails)
print(unique_emails)  # {'b@gmail.com', 'a@gmail.com'}


# Real-life backend example
users = [
    {"id": 1, "role": "admin"},
    {"id": 2, "role": "user"},
    {"id": 3, "role": "admin"},
]

admin_ids = set()
for user in users:
    if user["role"] == "admin":
        admin_ids.add(user["id"])

print(admin_ids)  # {1,3}
