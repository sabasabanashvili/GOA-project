# 11) Function to append a list of items to a list
def append_items(lst, items):
    lst.extend(items)

# 12) Function to append all elements of one list to another
def append_list_to_list(lst1, lst2):
    lst1.extend(lst2)

# 13) Function to insert an item at a specified index
def insert_item(lst, index, item):
    lst.insert(index, item)

# 14) Function to insert an item at the beginning of a list
def insert_at_beginning(lst, item):
    lst.insert(0, item)

# 15) Function to insert an item at the end of a list using the insert method
def insert_at_end(lst, item):
    lst.insert(len(lst), item)