#Capitalize the first letter of a sentence provided by the user.
sentence = input("Enter a sentence: ")
print(sentence.capitalize())
#Given a list of lowercase strings, capitalize the first letter of each string.
list_of_strings = ["hello", "world", "python"]
for string in list_of_strings:
    print(string.capitalize())
#Create a function that takes a string and returns it with the first letter capitalized.
def capitalize_first_letter(string):
    return string.capitalize()
name = input("Enter a name: ")
print(capitalize_first_letter(name))