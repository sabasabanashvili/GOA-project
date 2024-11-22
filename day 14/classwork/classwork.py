first_number = int(input("შეიყვანეთ პირველი რიცხვი: "))
second_number = int(input("შეიყვანეთ მეორე რიცხვი: "))

for i in range(first_number, second_number + 1):
    print(i ** 2)
    print(first_number * second_number)
    print(first_number - second_number)
    print(first_number + second_number)

num1, num2, num3=10, 70, 90
for i in range(num1, num2):
    print(i + num2)