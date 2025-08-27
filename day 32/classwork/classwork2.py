def manual_append(main_list, item_to_insert):
    main_list.insert(len(main_list), item_to_insert)
list=[1,2,3,4,5]
manual_append(list, 6)
print(list)