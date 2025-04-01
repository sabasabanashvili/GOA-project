try:
    number = float(input("შეიყვანეთ რიცხვი: "))
except ValueError:
    print("შეცდომა: უნდა შეიყვანოთ რიცხვი!")

my_list = [1, 2, 3]
try:
    print(my_list[5])
except IndexError:
    print("შეცდომა: მოცემული ინდექსი არ არსებობს სიაში!")

try:
    result = "ჩემი ასაკი: " + 25
except TypeError:
    print("შეცდომა: სტრიქონსა და მთელ რიცხვს შორის მიმატება შეუძლებელია!")