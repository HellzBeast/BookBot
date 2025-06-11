def word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    lowercase = text.lower()
    lower_dictionary = {}
    for char in lowercase:
        lower_dictionary[char] = lower_dictionary.get(char, 0) + 1
    return lower_dictionary

def char_count_sorted(text):
    char_list = []
    for char, count in char_count(text).items():
        char_list.append({"char": char, "num": count})
    char_list.sort(key=lambda x: x["num"], reverse=True)
    return char_list