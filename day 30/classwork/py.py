def manual_swapcase(text):
    result = ""
    for char in text:
        if char.islower():
            result += char.upper()
        elif char.isupper():
            result += char.lower()
        else:
            result += char
    print(result) 

manual_swapcase("Hello World!")