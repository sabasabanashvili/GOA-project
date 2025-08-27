set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 | set2)
print(set1 & set2)
print(set1 - set2)

my_set = {1, 2, 3, 4, 5}
my_set.add(6)
my_set.remove(3)
print(6 in my_set)

my_list = [1, 2, 2, 3, 3, 4]
my_list = list(set(my_list))
print(my_list)
