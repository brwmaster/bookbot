def main():
    book_path = "./books/frankenstein.txt"
    book_content = get_book_content(book_path)
    print(book_content)


def get_book_content(path):
    with open(path) as f:
        return f.read()


main()
