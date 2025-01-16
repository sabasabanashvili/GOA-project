#Find the position of the first occurrence of the word "Python" in a sentence.
sentence = "Learning Python is fun with Python tutorials."
print(sentence.find("Python"))
#Search for a user-specified substring and print its starting index:
string = "This is a simple string example."
substring = input("Enter a substring: ")
print(string.find(substring)) 
#Write a function to find and return the index of a specified character in a given string.
def find_char(string, char):
    return string.find(char)
print(find_char("Hello, World!", "o"))