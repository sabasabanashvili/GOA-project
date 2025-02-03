#Find the Maximum Create a function that takes a list of numbers and uses a loop to find and return the maximum number.
def find_max(numbers):
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]