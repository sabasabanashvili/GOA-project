#Define a function that takes a list of integers and returns a new list containing only the positive numbers. Use a loop and a conditional statement.
def positive_numbers(numbers):
    positive = []
    for num in numbers:
        if num > 0:
            positive.append(num)
    return positive

numbers = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]