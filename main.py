def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    char_count = get_char_count(text)
    print_report(word_count, char_count, book_path)

def get_book_text(path):
    with open(path, mode='r') as file:
        return file.read()

def get_word_count(text):
    return len(text.split())

def get_char_count(text):
    word_dict = {}
    for e in text:
        if e.isalpha():
            char = e.lower()
            word_dict[char] = word_dict.get(char, 0) + 1
    return word_dict

def sort_char_dict(char_dict):
    def sort_func(pair):
        return pair[1]

    char_list = []
    for letter, count in char_dict.items():
        char_list.append((letter, count))
    char_list.sort(reverse=True, key=sort_func)
    return char_list

def print_report(word_count, char_dict, path):
    char_list = sort_char_dict(char_dict)

    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document\n")
    for pair in char_list:
        print(f"The '{pair[0]}' character was found {pair[1]} times")
    print("--- End report ---")

main()