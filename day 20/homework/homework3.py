num1 = int(input("Enter a number: "))
is_valid = True
for i in range(2, num1):
    if num1 % i == 0:
        is_valid = False

if is_valid == True:
    print("Prime")
else:
    print("Not Prime")