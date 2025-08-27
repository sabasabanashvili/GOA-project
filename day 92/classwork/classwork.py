def round_to_next5(n):
    if n%5 == 0: return n

    return (n//5 + 1) * 5
Round up to the next multiple of 5
def two_oldest_ages(ages):
    ages = sorted(ages)

    return [ages[-2], ages[-1]]
    
def two_oldest_ages(ages):
    return sorted(ages)[-2:]

def gimme(input_array):
    # input_array = [10, 5, 2]

    sorted_arr = sorted(input_array)
    # sorted_arr = [2, 5, 10]

    mid_l = sorted_arr[1]
    # mid_l = 5

    return input_array.index(mid_l)
    # [10, 5, 2].index(5) = 1
Find the middle element
def angle(n):
    return (n-2)*180
def capitalize(s):
    even = [s[i].upper() if i % 2 == 0 else s[i] for i in range(len(s))  ]
    odd = [s[i].upper() if i % 2 != 0 else s[i] for i in range(len(s))  ]
    return ["".join(even),"".join(odd)]