def fix_the_meerkat(arr):
    return arr[::-1]

def grab_city(txt):
    return txt[txt.find("[") + 1:txt.find("]")]

def repeat_it(string, n):
    return ' '.join([string] * n)

def broken_counter(n):
    return n // 10 + (n % 10) // 5 + (n % 5)

def adding_shifted(arrays, shift):
    result = []
    for i, arr in enumerate(arrays):
        for j, val in enumerate(arr):
            index = j + i * shift
            if index >= len(result):
                result.extend([0] * (index + 1 - len(result)))
            result[index] += val
    return result
