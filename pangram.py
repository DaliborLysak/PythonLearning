import string

def pangram(sentence, alphabet=string.ascii_lowercase):
    sentence = sentence.replace(' ', '')
    sentence = sentence.lower()
    word_set = set()
    word_set.update(sentence)
    word_list = list(word_set)
    word_list.sort(key=str.lower)
    value = ''.join(word_list)
    # print(value)
    return alphabet == value

# Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog"
print("Write a sentence for pangram test:")
sentence = input()
result = pangram(sentence)
print("It is pangram" if result else "It is not pangram")