#1
def divide_numbers():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 / num2
        print(f"The result of division is: {result}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except ValueError:
        print("Error: Please enter valid numbers.")

divide_numbers()

#2
def access_list_index():
    my_list = [10, 20, 30, 40, 50]
    try:
        index = int(input("Enter an index to access: "))
        print(f"The element at index {index} is: {my_list[index]}")
    except IndexError:
        print("Error: Index out of range.")
    except ValueError:
        print("Error: Please enter a valid integer.")

access_list_index()

#3
def convert_to_integer():
    try:
        user_input = input("Enter a number: ")
        number = int(user_input)
        print(f"The number you entered is: {number}")
    except ValueError:
        print("Error: That is not a valid number.")

convert_to_integer()

#4
def greet_user(greeting_function):
    greeting_function()

def say_hello():
    print("Hello, welcome to the program!")

greet_user(say_hello)

#5
def multiplier(factor):
    def multiply(number):
        return number * factor
    return multiply

multiply_by_3 = multiplier(3)
result = multiply_by_3(5)
print(f"5 multiplied by 3 is: {result}")
