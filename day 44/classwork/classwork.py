#1
def past(h, m, s):
    sum_of_seconds = 0
    
    # hour -> second
    sum_of_seconds += h * 3600
    
    # minute -> second
    sum_of_seconds += m * 60
    
    # second
    sum_of_seconds += s
    
    # result
    result = sum_of_seconds * 1000
    
    return result
#2
def abbrev_name(name):
    new_list = name.split(" ")
    return f"{new_list[0][0].upper()}.{new_list[1][0].upper()}"

#3
def find_needle(haystack):
    result = haystack.index("needle")
    return f"found the needle at position {result}"
#4
def invert(lst):
    new_list=[]
    for i in lst:
        new_list.append(i * -1)
    return new_list
#5
def invert(lst):
    new_list = []
    for i in lst:
        new_list.append(i* -1)
    return new_list
#6
def smash(words):
    return " ".join(words)
#7
def grow(arr):
    product = 1

    for i in arr:
        product *= i

    return product
#8
def better_than_average(class_points, your_points):
    other_avg = sum(class_points) / len(class_points)

    if your_points > other_avg: return True
    return False
#9
def zero_fuel(distance_to_pump, mpg, fuel_left):
    if mpg * fuel_left >= distance_to_pump:
        return True
    return False