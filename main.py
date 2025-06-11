def get_book_text(filepath):
    with open(filepath) as file:
        text = file.read()
    return text

from stats import word_count
from stats import char_count
from stats import char_count_sorted

def main():
    book_path = "books/frankenstein.txt"
    content = get_book_text(book_path)
    count = word_count(content)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for dictionary in char_count_sorted(content):
        char = dictionary["char"]
        count = dictionary["num"]
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")
main()