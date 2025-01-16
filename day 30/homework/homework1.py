#Convert all the characters of a given sentence to lowercase and print it.
name = "davita"
print(name.lower())

#Ask the user for their email address and ensure it is stored in lowercase.
email = input("Enter your email: ")
print(email.lower())

#Write a function that takes a mixed-case string and returns it in all lowercase letters.
def convert_to_lowercase(string):
    return string.lower()
print(convert_to_lowercase("DaviTa"))