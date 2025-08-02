# 1) Find the first non-consecutive number
def first_non_consecutive(arr):
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1] + 1:
            return arr[i]
    return None

# 2) Sort Numbers
def solution(nums):
    return sorted(nums) if nums else []

# 3) Make a number negative
def make_negative(number):
    return -abs(number)

# 4) Replace With Alphabet Position
def alphabet_position(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())

# 5) Anagram Detection
def is_anagram(test, original):
    return sorted(test.lower()) == sorted(original.lower())

# ტესტები
if __name__ == "__main__":
    print("1) First Non-Consecutive:")
    print(first_non_consecutive([1, 2, 3, 4, 6]))  # ➜ 6

    print("\n2) Sorted Numbers:")
    print(solution([5, 2, 1, 4, 3]))  # ➜ [1, 2, 3, 4, 5]

    print("\n3) Make Negative:")
    print(make_negative(5))   # ➜ -5
    print(make_negative(-3))  # ➜ -3

    print("\n4) Alphabet Position:")
    print(alphabet_position("The sunset sets at twelve o' clock."))  
    # ➜ '20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11'

    print("\n5) Anagram Detection:")
    print(is_anagram("foefet", "toffee"))  # ➜ True
    print(is_anagram("Buckethead", "DeathCubeK"))  # ➜ True
