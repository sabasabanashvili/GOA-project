student = {
    "name": "Emma",
    "age": 21,
    "major": "Mathematics"
}

# Using get() to retrieve a value
gpa = student.get("GPA", "Key not found")
print(gpa)  # Output: Key not found