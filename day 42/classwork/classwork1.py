# Initialize the dictionary with at least five key-value pairs
my_dict = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York',
    'occupation': 'Engineer',
    'hobby': 'Reading'
}

# Print all the keys in the dictionary
print("Keys in the dictionary:")
print(my_dict.keys())

# Print all the values in the dictionary
print("\nValues in the dictionary:")
print(my_dict.values())

# Print all key-value pairs in the dictionary
print("\nKey-Value pairs in the dictionary:")
print(my_dict.items())

# Iterate over the dictionary and print each key with its corresponding value
print("\nIterating over the dictionary:")
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")
