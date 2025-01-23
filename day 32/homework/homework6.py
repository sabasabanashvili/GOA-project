def split_into_sentences(paragraph):
    return paragraph.split('.')

paragraph = input("Enter Your string: ")
sentences = split_into_sentences(paragraph)
print(sentences)
