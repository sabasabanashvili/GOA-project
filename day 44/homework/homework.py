# 1. Clock
def past(h, m, s):
    return (h * 3600 + m * 60 + s) * 1000

# 2. Abbreviate a Two Word Name
def abbrev_name(name):
    return ".".join([word[0] for word in name.upper().split()])

# 3. How many lightsabers do you own?
def how_many_light_sabers_do_you_own(name=""):
    return 18 if name == "Zach" else 0

# 4. Invert values
def invert(lst):
    return [-x for x in lst]

# 5. Define a card suit
def define_suit(card):
    suits = {'♣': 'clubs', '♦': 'diamonds', '♥': 'hearts', '♠': 'spades'}
    return suits[card[-1]]

# 6. Sentence Smash
def smash(words):
    return " ".join(words)

# 7. Beginner - Reduce but Grow
from math import prod
def grow(arr):
    return prod(arr)

# 8. Find the Remainder
def remainder(a, b):
    if a == 0 or b == 0:
        return None
    return max(a, b) % min(a, b)

# 9. Reversed sequence
def reverse_seq(n):
    return list(range(n, 0, -1))

# 10. Opposites Attract
def lovefunc(flower1, flower2):
    return (flower1 + flower2) % 2 == 1

# 11. Will you make it?
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return distance_to_pump <= mpg * fuel_left

# 12. Is it a palindrome?
def is_palindrome(s):
    return s.lower() == s[::-1]

# 13. Find Maximum and Minimum Values of a List
def minimum(arr):
    return min(arr)

def maximum(arr):
    return max(arr)

# 14. Remove String Spaces
def no_space(x):
    return x.replace(" ", "")

# 15. Check if a number is even or odd
def even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"

# 16. You Can't Code Under Pressure #1
def double_integer(i):
    return i * 2

# 17. Rock Paper Scissors
def rps(p1, p2):
    outcomes = {"scissors": "paper", "paper": "rock", "rock": "scissors"}
    if p1 == p2:
        return "Draw!"
    return "Player 1 won!" if outcomes[p1] == p2 else "Player 2 won!"

# 18. Is n divisible by x and y?
def is_divisible(n, x, y):
    return n % x == 0 and n % y == 0

# 19. Count sheep
def count_sheep(n):
    return "".join(f"{i} sheep..." for i in range(1, n+1))

# 20. Get Grade
def get_grade(s1, s2, s3):
    avg = (s1 + s2 + s3) / 3
    return "ABCDF"[max(0, 4 - (avg // 10 - 5))]
