# 2) Lambda function to add 5 to a number
add_five = lambda x: x + 5
print("Add 5:", add_five(10))

# 3) Lambda function to multiply two numbers
multiply = lambda x, y: x * y
print("Multiply:", multiply(3, 4))

# 4) Lambda function to check if a number is even
is_even = lambda x: x % 2 == 0
print("Is even:", is_even(6))

# 5) Lambda function to convert Celsius to Fahrenheit
c_to_f = lambda c: (c * 9/5) + 32
print("Celsius to Fahrenheit:", c_to_f(0))

# 6) Lambda function to check if a string starts with 'A'
starts_with_A = lambda s: s.startswith('A')
print("Starts with A:", starts_with_A('Apple'))

# 7) Use map() to add 10 to every number in a list
nums = [1, 2, 3, 4, 5]
add_10 = list(map(lambda x: x + 10, nums))
print("Add 10 to each:", add_10)

# 8) Use map() to convert strings to uppercase
words = ['apple', 'banana', 'cherry']
uppercased = list(map(lambda s: s.upper(), words))
print("Uppercased words:", uppercased)

# 9) Use map() to find length of each word
lengths = list(map(lambda s: len(s), words))
print("Lengths:", lengths)

# 10) Use map() to square each number
squared = list(map(lambda x: x**2, nums))
print("Squared numbers:", squared)

# 11) Use map() to convert integers to strings
nums_as_str = list(map(lambda x: str(x), nums))
print("Integers as strings:", nums_as_str)

# 12) Use map() to concatenate "Hello " to each name
names = ['Alice', 'Bob', 'Charlie']
greeted = list(map(lambda name: "Hello " + name, names))
print("Greeted names:", greeted)

# 13) Use map() to subtract 5 from every element
subtract_5 = list(map(lambda x: x - 5, nums))
print("Subtract 5 from each:", subtract_5)

# 14) Use map() to multiply each number by 3
times_3 = list(map(lambda x: x * 3, nums))
print("Multiply by 3:", times_3)

# 15) Use map() to convert Celsius to Fahrenheit
temps_c = [0, 20, 30, 40]
temps_f = list(map(lambda c: (c * 9/5) + 32, temps_c))
print("Temps in Fahrenheit:", temps_f)

# 16) Use map() to check if numbers > 50
nums2 = [10, 60, 30, 80, 45]
greater_50 = list(map(lambda x: x > 50, nums2))
print("Greater than 50:", greater_50)

# 17) Use filter() to keep only even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, nums2))
print("Even numbers:", even_numbers)

# 18) Use filter() to select numbers > 10
greater_than_10 = list(filter(lambda x: x > 10, nums))
print("Numbers > 10:", greater_than_10)

# 19) Use filter() to keep strings longer than 5 characters
long_words = list(filter(lambda s: len(s) > 5, words))
print("Words longer than 5 chars:", long_words)

# 20) Use filter() to remove empty strings
strings = ['hello', '', 'world', '', 'python']
non_empty = list(filter(lambda s: s != '', strings))
print("Non-empty strings:", non_empty)

# 21) Use filter() to select only positive numbers
mixed_nums = [-5, 0, 5, 10, -2]
positive_nums = list(filter(lambda x: x > 0, mixed_nums))
print("Positive numbers:", positive_nums)

# 22) Use filter() to keep names starting with 'A'
names2 = ['Alice', 'Bob', 'Amanda', 'Charlie']
names_starting_A = list(filter(lambda name: name.startswith('A'), names2))
print("Names starting with A:", names_starting_A)

# 23) Use filter() to get numbers divisible by 3
div_by_3 = list(filter(lambda x: x % 3 == 0, nums2))
print("Divisible by 3:", div_by_3)

# 24) Use filter() to keep words containing 'e'
words2 = ['tree', 'apple', 'sky', 'cloud']
words_with_e = list(filter(lambda w: 'e' in w, words2))
print("Words containing 'e':", words_with_e)

# 25) Use filter() to remove None values
list_with_none = [1, None, 2, None, 3]
without_none = list(filter(lambda x: x is not None, list_with_none))
print("Without None values:", without_none)

# 26) Use filter() to keep numbers <= 50
less_equal_50 = list(filter(lambda x: x <= 50, nums2))
print("Numbers <= 50:", less_equal_50)

