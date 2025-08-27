number = str(5)
user_number = str(input("Enter Num: "))
counter = 0

while user_number < number:
    print("Wrong Number")
    user_number=input("Try again: ")
    counter += 1

print("sucsess")
print(str(counter))