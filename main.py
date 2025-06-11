def get_book_text(filepath):
    with open(filepath) as file:
        text = file.read()
    return text

def main():
    book_path = "books/frankenstein.txt"
    content = get_book_text(book_path)
    print(content)
