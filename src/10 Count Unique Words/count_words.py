import re
import collections


def count_words(filename: str):
    word_counter = {}
    word_pattern = r"([A-Z|a-z|0-9|\-']+)"
    with open(filename, 'r') as fhandle:
        while line := fhandle.readline():
            words = re.findall(word_pattern, line)
            for word in words:
                word = word.upper()
                if word in word_counter:
                    word_counter[word] += 1
                else:
                    word_counter[word] = 1

    word_counter = sorted(word_counter.items(), key=lambda item: item[1], reverse=True)
    print(f'Total Unique Words: {len(word_counter)}')
    print('Top 20 words:')
    
    for i in range(0, 20):
        print(f'{word_counter[i][0]}: {word_counter[i][1]}')


# commands used in solution video for reference
if __name__ == '__main__':
    count_words('shakespeare.txt')
