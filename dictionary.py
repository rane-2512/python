# Creating a dictionary
student = {
    "name": "Tanvi",
    "age": 18,
    "course": "Computer Science"
}

print("Dictionary:", student)

# Accessing a value
print("Name:", student["name"])

# Adding a new item
student["city"] = "Pune"
print("After adding:", student)

# Updating a value
student["age"] = 19
print("After updating:", student)

# Removing an item
student.pop("city")
print("After removing:", student)

# Dictionary functions
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

# Checking if a key exists
print("name" in student)

# Length of dictionary
print("Length:", len(student))
