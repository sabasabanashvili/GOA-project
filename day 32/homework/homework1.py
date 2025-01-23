#Write a function that takes a first name and last name, capitalizes them, and formats them into a single string without return.
def format_name(first_name, last_name):
    print(first_name.capitalize() + " " + last_name.capitalize())
print(format_name(input("Enter First Name: "), input("Enter Last Name: ")))