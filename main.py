def main():
    book_path = "./books/frankenstein.txt"
    book_content = get_book_content(book_path)
    word_count = count_words(book_content)
    char_count = count_chars(book_content)
    list_of_chars = dict_to_list(char_count)
    generate_report(word_count, list_of_chars)


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


def sort_on(dict):
    return list(dict.values())[0]


def dict_to_list(dict):
    return [{k: v} for k, v in dict.items()]


def generate_report(word_count, list_of_chars):
    list_of_chars.sort(key=sort_on, reverse=True)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")

    for item in list_of_chars:
        for char, count in item.items():
            if char.isalpha():
                print(f"The '{char}' character was found {count} times")

    print("\n--- End of report ---")


main()
