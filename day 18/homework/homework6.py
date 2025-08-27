num1 = float(input("Enter a number: "))
ope = str(input("Enter an operator(+,-,*,/): "))
num2 = float(input("Enter a number: "))

if ope == "+":
    result = num1 + num2
if ope == "-":
    result = num1 - num2
if ope == "*":
    result = num1 * num2
if ope == "/":
    result = num1 / num2

print("Result is:", num1, ope, num2, "=" , result)
