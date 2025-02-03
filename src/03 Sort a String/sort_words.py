def sort_words(words):
    word_dict = {str.casefold(word): word  for word in words.split(' ')}
    word_dict = dict(sorted(word_dict.items()))
    words = list(word_dict.values())
    return ' '.join(words)


# commands used in solution video for reference
if __name__ == '__main__':
    print(sort_words('banana ORANGE apple'))  # apple banana ORANGE
