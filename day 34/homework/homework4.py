#Write a function that takes a list of numbers and checks whether each number is even or odd using a loop and conditional statements. Print "Even" for even numbers and "Odd" for odd numbers.
def check_even_odd(numbers):
    for number in numbers:
        if number % 2 == 0:
            print("Even")
        else:
            print("Odd")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]