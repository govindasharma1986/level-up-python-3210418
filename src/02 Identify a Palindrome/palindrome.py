import re
import string

def is_palindrome(phrase: str) -> bool:
    forward_phrase = ''
    for ch in phrase.lower():
        if ch in string.ascii_lowercase:
            forward_phrase += ch
    
    backward_phrase = reversed(forward_phrase)
    return forward_phrase == backward_phrase

# commands used in solution video for reference
if __name__ == '__main__':
    print(is_palindrome('hello world'))  # false
    print(is_palindrome("Go hang a salami, I'm a lasagna hog."))  # true
