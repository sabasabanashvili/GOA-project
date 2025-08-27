num1, num2= int(input("Enter numbers: ")), int(input("Enter numbers: "))
if num1 > num2:
    DD = range(num1, num2-1, +1)
    sum=0

    for i in DD:
        i %2 == 0
        sum += i
    print(sum)
else:
    range2 = range(num1, num2 + 1)
    sum2 = 0

    for i in range2:
        if i %2 == 0:
            sum2 += i
    print(sum2)
    print(i)
print("The sum of even numbers is: ", str(sum2))