name = str(input("Enter your name: "))
choice=str(input("Enter your choice (u or l): "))
if choice == "u":
    print(name.upper())
elif choice == "l":
    print(name.lower())
else:
    print("Invalid choice")