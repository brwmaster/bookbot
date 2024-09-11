def main():
    book_path = "./books/frankenstein.txt"
    book_content = get_book_content(book_path)
    word_count = count_words(book_content)
    char_count = count_chars(book_content)


def get_book_content(path):
    with open(path) as f:
        return f.read()


def count_words(content):
    return len(content.split())


def count_chars(content):
    for char in content:
        print(char)


main()
