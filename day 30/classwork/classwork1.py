def manual_find(main_string, str_to_find):
    i = 0
    main_len = 0
    find_len = 0

    for _ in main_string:
        main_len += 1
    for _ in str_to_find:
        find_len += 1

    while i <= main_len - find_len:
        match = True
        for j in range(find_len):
            if main_string[i + j] != str_to_find[j]:
                match = False
                break
        if match:
            return i
        i += 1

    return -1

# Testing
print(manual_find("hello world", "world"))  # 6
print(manual_find("hello world", "python"))  # -1
print(manual_find("abcdef", "def"))  # 3
print(manual_find("abcdef", "gh"))  # -1
