#Find and print the index of the first occurrence of the word "hello" in a given string.
string = "hello world, hello everyone"
print(string.find("hello"))
#Write a function that returns the index of a character provided by the user in a string.
def find_index(string, char):
    return string.find(char)
print(find_index("hello world, hello everyone", "e"))
