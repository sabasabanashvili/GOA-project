def my_split(main_string, string_to_split):
    # დაყოფა string_to_split-ის მიხედვით
    result = main_string.split(string_to_split)
    print(result)

# მომხმარებლისგან შემოსული მონაცემები
main_string = input("შეიყვანეთ მთავარი ტექსტი: ")
string_to_split = input("შეიყვანეთ ტექსტი, რომლის მიხედვითაც უნდა გაიხლიჩოს: ")

# ფუნქციის გამოძახება
my_split(main_string, string_to_split)
