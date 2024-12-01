my_password = "5123"
user_guess=input("Enter the password: ")
counter = 0 

while my_password != user_guess:
    print("Wrong Password")
    user_guess=input("Enter the password: ")
    counter += 1 

print("You Got It")
print("Password was entered", str(counter), "times.")
