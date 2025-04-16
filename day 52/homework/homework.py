# Remove all exclamation marks from a string
def remove_exclamation_marks(s):
    return s.replace("!", "")

# Remove exclamation marks from the end of a string
def remove(s):
    return s.rstrip("!")

# Convert number to reversed array of digits
def digitize(n):
    return list(map(int, str(n)[::-1]))

# Convert each letter in a string to the opposite case
def alternate_case(s):
    return s.swapcase()

# Capitalize the first letter of each word
def capitalize(s):
    return s.title()

# Always return a negative version of a number
def make_negative(n):
    return -abs(n)

# Repeat each character in a string n times
def repeat_char(s, n):
    return "".join(char * n for char in s)

# Is number divisible by x and y?
def is_divisible(n, x, y):
    return n % x == 0 and n % y == 0

# Keep Hydrated!
def litres(time):
    return time // 2

# Reverse Words
def reverse_words(str):
    return " ".join(str.split()[::-1])

# Cockroach Speed
def cockroach_speed(s):
    return int(s * 27.7778)

# Will you make it?
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return distance_to_pump <= mpg * fuel_left

# Sum of Positive
def positive_sum(arr):
    return sum(x for x in arr if x > 0)

# Sum Arrays
def sum_array(a):
    return sum(a)

# Count Sheep
def count_sheep(n):
    return "".join(f"{i} sheep..." for i in range(1, n+1))

# How Old Are You?
def get_age(age):
    return int(age[0])

# Convert a Boolean to a String
def boolean_to_string(b):
    return str(b)

# String Repeat
def repeat_str(n, s):
    return s * n

# Remove Spaces
def no_space(x):
    return x.replace(" ", "")

# Basic Mathematical Operations
def basic_op(operator, value1, value2):
    return eval(f"{value1}{operator}{value2}")

# Remove all exclamation marks from a string
def remove_exclamation_marks(s):
    return s.replace("!", "")

# Remove exclamation marks from the end of a string
def remove(s):
    return s.rstrip("!")

# Convert number to reversed array of digits
def digitize(n):
    return list(map(int, str(n)[::-1]))

# Convert each letter in a string to the opposite case
def alternate_case(s):
    return s.swapcase()

# Capitalize the first letter of each word
def capitalize(s):
    return s.title()

# Always return a negative version of a number
def make_negative(n):
    return -abs(n)

# Repeat each character in a string n times
def repeat_char(s, n):
    return "".join(char * n for char in s)
