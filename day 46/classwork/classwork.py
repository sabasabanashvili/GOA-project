def manual_list(start, end, step, user_num):
    result = []
    for num in range(start, end, step):
        result.append(num + user_num)
    return result

# გამორთვა 3-ჯერ განსხვავებული არგუმენტებით
print(manual_list(1, 10, 2, 5))  # მაგალითი 1
print(manual_list(5, 20, 3, 10)) # მაგალითი 2
print(manual_list(0, 15, 4, 3))  # მაგალითი 3
