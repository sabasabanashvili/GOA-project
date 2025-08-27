def getCount(inputStr):
    return sum(1 for char in inputStr if char in 'aeiou')
