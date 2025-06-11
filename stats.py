def word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    lowercase = text.lower()
    lower_dictionary = {}
    for char in lowercase:
        lower_dictionary[char] = lower_dictionary.get(char, 0) + 1
    return lower_dictionary