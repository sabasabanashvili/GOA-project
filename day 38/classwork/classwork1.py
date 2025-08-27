def no_duplicates(user_list):
    new_list = []
    for i in user_list:
        if i not in new_list:
            new_list.append(i)
    return new_list


no_duplicates([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
no_duplicates([9,8,7,6,5,4,3,2,1,1,2,3,4,5,6,7,8,9,10,10,9,8,7,6,5,4,3,2,1])