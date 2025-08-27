        res += f"{i} * {number} = {i*number}\n"
    return res[0:-1]


# Super Duper Easy
def problem(a):
    if type(a) == str: return "Error"
    return a*50+6

# Grasshopper - If/else syntax debug
def check_alive(health):
    if health > 0:
        return True
    else:
        return False



# Grasshopper - Basic Function Fixer
def add_five(num):
    total = num + 5
    return total


# Grasshopper - Terminal game combat function
def combat(health, damage):
    if health - damage > 0: return health - damage
    return 0


# Capitalization and Mutability
def capitalize_word(word: str) -> str:
    return word[0].upper() + word[1:]



# How many lightsabers do you own?
def how_many_light_sabers_do_you_own(name=''):
    return 18 if name == 'Zach' else 0


def how_many_light_sabers_do_you_own(*args):
    if len(args) == 0: return 0
    return 18 if args[0] == "Zach" else 0



# Stringy Strings
def stringy(size):
    return ''.join('1' if i % 2 == 0 else '0' for i in range(size))