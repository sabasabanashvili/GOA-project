#Create a function that takes a string of comma-separated values (CSV) and returns a list of individual items.
def reserve(string):
    print(string.split(","))
reserve(input("Enter string: "))