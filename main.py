def main():
    book_path = "./books/frankenstein.txt"
    book_content = get_book_content(book_path)
    word_count = count_words(book_content)
    char_count = count_chars(book_content)
    print(f"Word count: {word_count}")
    print(f"Character count: {char_count}")


def get_book_content(path):
    with open(path) as f:
        return f.read()


def count_words(content):
    return len(content.split())


def count_chars(content):
    chars_count = {}
    for char in content.lower():
        if char in chars_count:
            chars_count[char] += 1
        else:
            chars_count[char] = 1

    return chars_count


main()
