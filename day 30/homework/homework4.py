#Find and print the length of a user-provided string.
string = input("Enter a string: ")
print(len(string))
#Write a function that takes a list of strings and returns their lengths.
def list_of_strings(list):
    for i in list:
        print(len(i))
list_of_strings(["Hello", "World", "Python", "Programming"])