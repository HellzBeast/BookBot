def get_book_text(filepath):
    with open(filepath) as file:
        text = file.read()
    return text

def word_count(text):
    words = text.split()
    return len(words)

def main():
    book_path = "books/frankenstein.txt"
    content = get_book_text(book_path)
    count = word_count(content)
    print(f"{count} words found in the document")
main()