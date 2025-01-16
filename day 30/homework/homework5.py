#Count the number of times the word "the" appears in a given paragraph.
paragraph = input("Enter a paragraph: ")
counter = 0
for word in paragraph.split():
    if word == "the":
        counter += 1
print(counter)
#Ask the user to input a character and count its occurrences in a given string.
name = input("Enter a name: ")
for i in name:
    if i == "a":
        counter += 1
print(counter)
#Create a function that counts and returns the occurrences of a specified word in a text.
def count_word(word, text):
    counter = 0
    for i in text.split():
        if i == word:
            counter += 1
    return counter
print(count_word("the", "the quick brown fox jumps over the lazy dog"))