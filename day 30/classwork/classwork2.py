main_str = str(input("Enter main string: "))
str_to_count = str(input("Enter string to count: "))

counter = 0
for i in range(len(main_str)):
    if main_str[i:i+len(str_to_count)] == str_to_count:
        counter += 1
print(counter)