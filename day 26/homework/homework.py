# 2) Sum of Two Numbers
def sum_of_two_numbers(a, b):
    print(a + b)

# 3) Even or Odd
def is_even_or_odd(number):
    print("Even" if number % 2 == 0 else "Odd")

# 4) Reverse a String
def reverse_string(s):
    print(s[::-1])

# 5) Find Maximum
def find_maximum(numbers):
    print(max(numbers))

# 6) Factorial
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    print(result)
