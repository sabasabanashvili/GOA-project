username = "saba"
inuser = input("Enter Your username: ")
password = "1234"
userPassword = input("Enter Your password: ")
count = 0
while username != inuser or password != userPassword:
    print("Wrong username or password")
    print(input("Enter your Username: "))
    print(input("Enter your password: "))
    count += 1
print("Congrats")

