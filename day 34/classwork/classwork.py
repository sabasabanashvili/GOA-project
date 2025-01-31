def remove_elements(main_list, indexes_list):
    for index in indexes_list:
        main_list.pop(index)
main_list = [10, 20, 30, 40, 50]
indexes_list = [1, 3]

remove_elements(main_list, indexes_list)
print(main_list)