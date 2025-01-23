#Write a function that takes a sentence, a word, and an index, and inserts the word into the sentence at the given index without return
def insert_word(sentence, word, index):
    sentence = sentence[:index] + word + sentence[index:]
    print(sentence)
print(insert_word("Hello World", "Python", 6))