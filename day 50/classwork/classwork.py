try:
    num = 10  
    num += "5"  
except TypeError:
    print("შეცდომა: ტიპების შეუთავსებლობა")

try:
    user_input = input("შეიყვანეთ თქვენი სახელი: ")
    if not user_input.strip():
        raise ValueError("სახელი არ არის ჩაწერილი")
    print(f"მოგესალმებით, {user_input}!")
except ValueError:
    print("დაფიქსირდა ValueError: შეყვანილი სახელი არ არის სწორი")
except Exception:
    print("დაფიქსირდა უცნობი შეცდომა")
