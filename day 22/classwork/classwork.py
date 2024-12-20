list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num1 = int(input("Enter a number: "))

if 0 < num1 < 10:
    print(list[num1])

elif -10 < num1 < -1:
    print(list(num1))

else:
    print("არასწორი შეყვანაა შეჩ")