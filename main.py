def main():
    book_path = "./books/frankenstein.txt"
    book_content = get_book_content(book_path)
    word_count = count_words(book_content)
    print(f"Word count: {word_count}")


def get_book_content(path):
    with open(path) as f:
        return f.read()


def count_words(content):
    return len(content.split())


main()
