def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = count_words(text)
    characters = count_characters(text)

    create_report(book_path, words, characters)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    return len(text.split())

def count_characters(text):
    char_count = {}
    for char in text:
        if char.lower() in char_count:
            char_count[char.lower()] += 1
        else:
            char_count[char.lower()] = 1
    
    return char_count

def get_chars_sorted(characters):
    return sorted(characters.items(), key=lambda item: item[1], reverse=True)

def create_report(path, words, characters):
    sorted_list = get_chars_sorted(characters)
    
    print(f"--- Begin report of {path} ---")
    print(f"{words} words where found in the document \n")

    for char in sorted_list:
        if char[0].isalpha():
            print(f"the {char[0]} character appears {char[1]} times")

    print(f"\n--- End report ---")

main()