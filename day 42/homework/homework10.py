def sum_numeric_values(d):
    return sum(value for value in d.values() if isinstance(value, (int, float)))

# Example dictionary
data = {"a": 10, "b": 20, "c": "hello", "d": 5.5}

# Calling function
print(sum_numeric_values(data))  # Output: 35.5
