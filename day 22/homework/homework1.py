my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

num1 = int(input("მიუთითეთ პირველი რიცხვი (num1): "))
num2 = int(input("მიუთითეთ მეორე რიცხვი (num2): "))

if num1 > num2:
    print(my_list[num2:num1])

elif num2 > num1:
    print(my_list[num1:num2])

else:
    print("num1 და num2 ერთიანია")