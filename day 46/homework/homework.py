# 2) List of numbers from 1 to 10
numbers = [x for x in range(1, 11)]

# 3) List of squares of numbers from 1 to 5
squares = [x**2 for x in range(1, 6)]

# 4) List of all even numbers between 1 and 20
evens = [x for x in range(1, 21) if x % 2 == 0]

# 5) First letters of each word in a given list of words
words = ["apple", "banana", "cherry"]
first_letters = [word[0] for word in words]

# 6) Convert all words in a given list to uppercase
uppercase_words = [word.upper() for word in words]

# 7) List of numbers from 1 to 50 that are divisible by 3
div_by_3 = [x for x in range(1, 51) if x % 3 == 0]

# 8) Extract words with more than 4 letters from a given list of words
long_words = [word for word in words if len(word) > 4]

# 9) Convert Celsius to Fahrenheit
celsius = [0, 10, 20, 30, 40]
fahrenheit = [(temp * 9/5) + 32 for temp in celsius]

# 10) Find all prime numbers between 1 and 100
primes = [x for x in range(2, 101) if all(x % y != 0 for y in range(2, int(x**0.5) + 1))]

# 11) Extract words from a sentence that contain at least one vowel and are longer than 5 characters
sentence = "List comprehensions are a powerful feature in Python programming"
vowels = "aeiouAEIOU"
words_in_sentence = sentence.split()
filtered_words = [word for word in words_in_sentence if len(word) > 5 and any(v in word for v in vowels)]

# 12) Generate a sequence of Fibonacci numbers up to the 20th term
fibonacci = [0, 1]
[fibonacci.append(fibonacci[-1] + f