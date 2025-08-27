# 2) Print your name
print("Saba")

# 3) Print a favorite quote
print('I rly Dont know')

# 4) Print multiple lines
print("Roses are red,\nViolets are blue,\nPython is great!")

# 5) Print a simple math result
print(2 + 3)

# 6) Print a shape with symbols
print("  *  \n *** \n*****")

# 7) Convert string to integer
num_str = "42"
num = int(num_str)
print(num)

# 8) Add two floats
num1 = 3.5
num2 = 2.5
print(num1 + num2)

# 9) Concatenate two strings
str1 = "Hello"
str2 = "World"
print(str1 + " " + str2)

# 10) Print data types
int_var = 5
str_var = "Python"
float_var = 3.14
print(type(int_var))
print(type(str_var))
print(type(float_var))

# 11) User input and type conversion
age = input("Enter your age: ")
age = int(age)
print("Next year, you will be", age + 1)

# 12) Ask for your name
name = input("What is your name? ")
print(f"Hello, {name}!")

# 13) Ask for age and calculate next year’s age
age = int(input("Enter your age: "))
print("Next year, you will be", age + 1)

# 14) Simple calculator: addition
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("The sum is:", num1 + num2)

# 15) Favorite color
color = input("What is your favorite color? ")
print(f"Your favorite color is {color}!")

# 16) Check if the user is tall enough
height = int(input("Enter your height in cm: "))
if height > 150:
    print("You are tall enough!")
else:
    print("Sorry, you are not tall enough.")

# 17) Print numbers from 1 to 5
for i in range(1, 6):
    print(i)

# 18) Print each letter of a string
word = "Python"
for letter in word:
    print(letter)

# 19) Sum of numbers 1 to 10
total = 0
for i in range(1, 11):
    total += i
print(total)

# 20) Print a multiplication table (1 to 5)
for i in range(1, 6):
    print(f"2 x {i} = {2 * i}")

# 21) Task: Use a for loop to print all even numbers between 2 and 20 (inclusive).
for i in range(2, 21, 2):
    print(i)

# 22) Print numbers from 1 to 5 using a while loop
i = 1
while i <= 5:
    print(i)
    i += 1

# 23) Sum of numbers 1 to 5 using a while loop
total = 0
i = 1
while i <= 5:
    total += i
    i += 1
print(total)

# 24) Count down from 10 to 1
i = 10
while i >= 1:
    print(i)
    i -= 1

# 25) Print all odd numbers between 1 and 10 using a while loop
i = 1
while i <= 10:
    if i % 2 != 0:
        print(i)
    i += 1

# 26) Ask for user input until they enter "exit"
user_input = ""
while user_input != "exit":
    user_input = input("Enter something (type 'exit' to stop): ")

# 27) Print all elements of a list
my_list = [1, 2, 3]
for item in my_list:
    print(item)

# 28) Find the length of a list
my_list = [1, 2, 3, 4, 5]
print(len(my_list))

# 29) Access a specific element from the list
my_list = [10, 20, 30]
print(my_list[1])  # Prints 20

# 30) Add an element to the list
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)

# 31) Remove an element from the list
my_list = [1, 2, 3]
my_list.remove(2)
print(my_list)

# 32) Create a list of squares
squares = [x**2 for x in range(1, 6)]
print(squares)

# 33) Create a list of even numbers
even_numbers = [x for x in range(2, 11, 2)]
print(even_numbers)

# 34) Filter odd numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7]
odd_numbers = [x for x in numbers if x % 2 != 0]
print(odd_numbers)

# 35) Convert a list of strings to uppercase
strings = ["hello", "world"]
uppercase_strings = [s.upper() for s in strings]
print(uppercase_strings)

# 36) Create a list of numbers squared if they are divisible by 2
numbers = [1, 2, 3, 4, 5]
squared_if_even = [x**2 for x in numbers if x % 2 == 0]
print(squared_if_even)

# 37) Function to greet a user
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

# 38) Function to add two numbers
def add_numbers(num1, num2):
    return num1 + num2

print(add_numbers(3, 5))

# 39) Function to check if a number is even or odd
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(check_even_odd(7))

# 40) Function to calculate the area of a rectangle
def calculate_area(length, width):
    return length * width

# Test the function
area = calculate_area(5, 3)
print("Area of the rectangle:", area)

# 41) Function to reverse a string
def reverse_string(s):
    return s[::-1]

# Test the function
reversed_str = reverse_string("hello")
print("Reversed string:", reversed_str)

# 42) Create and print a tuple
my_tuple = (10, "Hello", 3.14)
print("Tuple:", my_tuple)

# 43) Access an element in a tuple
my_tuple = (10, "Hello", 3.14)
print("Second element:", my_tuple[1])  # Index 1

# 44) Find the length of a tuple
my_tuple = (10, "Hello", 3.14)
print("Length of the tuple:", len(my_tuple))

# 45) Concatenate two tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2
print("Concatenated tuple:", concatenated_tuple)

# 46) Check if an item exists in a tuple
my_tuple = (1, 2, 3, 4, 5)
item = 3
if item in my_tuple:
    print("Found")
else:
    print("Not found")

# 47) Create and print a set
my_set = {1, 2, 3}
print("Set:", my_set)

# 48) Check if an element is in a set
my_set = {1, 2, 3, 4, 5}
element = 3
if element in my_set:
    print("Yes")
else:
    print("No")

# 49) Add an element to a set
my_set = {1, 2, 3}
my_set.add(4)
print("Updated set:", my_set)

# 50) Remove an element from a set
my_set = {1, 2, 3, 4}
my_set.remove(2)
print("Updated set:", my_set)

# 51) Find the union of two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2
print("Union of the sets:", union_set)

# 52) Create and print a dictionary
my_dict = {"name": "Alice", "age": 25}
print("Dictionary:", my_dict)

# 53) Access a value by key
my_dict = {"name": "Alice", "age": 25}
print("Value for 'name':", my_dict["name"])

# 54) Add a new key-value pair to a dictionary
my_dict = {"name": "Alice", "age": 25}
my_dict["city"] = "New York"
print("Updated dictionary:", my_dict)

# 55) Basic variable assignment task
name = "codewa.rs"
print("The name is:", name)

# 56) Function to get character from ASCII Value
def get_char_from_ascii(value):
    return chr(value)

# Test the function
print("Character for ASCII value 65:", get_char_from_ascii(65))  # Output will be 'A'
print("Character for ASCII value 97:", get_char_from_ascii(97))  # Output will be 'a'
print("Character for ASCII value 48:", get_char_from_ascii(48))  # Output will be '0'
