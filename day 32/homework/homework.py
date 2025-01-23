#Write a function that takes a user's name and age, and returns a welcome message formatted with an f-string.
def welcome(name, age):
    return f"Welcome {name}, you are {age} years old."
print(welcome(input("Enter your name: "), input("Enter your age: ")))