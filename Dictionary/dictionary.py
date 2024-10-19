# Basic dictionary hardcoded using a list of tuples
simple_dict = [
    ("name", "Alice"),
    ("age", 25),
    ("city", "New York")
]

# Accessing values manually
for key, value in simple_dict:
    if key == "name":
        print(f"Name: {value}")  # Output: Name: Alice
    if key == "age":
        print(f"Age: {value}")  # Output: Age: 25
    if key == "city":
        print(f"City: {value}")  # Output: City: New York
