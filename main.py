import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    book_path = sys.argv[1]

def get_book_text(filepath):
    with open(filepath) as file:
        text = file.read()
    return text

from stats import word_count
from stats import char_count
from stats import char_count_sorted

def main():
    content = get_book_text(book_path)
    count = word_count(content)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path} ")
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