#Convert a given sentence to uppercase and print the result.
name = "davita"
print(name.upper())
#Take a user's name input and display it in uppercase letters.
name = "davita"
print(name.upper())
#Create a function that converts a list of lowercase strings to uppercase.
def convert_to_uppercase(list):
    return [x.upper() for x in list]

low_cases=["davita","mike","john"]
print(convert_to_uppercase(low_cases))