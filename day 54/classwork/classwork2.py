# Function to apply a given function to all elements in a list
def apply_to_list(func, values):
    return [func(value) for value in values]

# Function to square a number
def square(x):
    return x * x

# Example usage
numbers = [1, 2, 3, 4, 5]
squared_numbers = apply_to_list(square, numbers)
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
