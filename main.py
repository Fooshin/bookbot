import sys
from stats import book_words, repeated_char, sorted_dict

if len(sys.argv) != 2:
    print("Usage: python3 main.py ,path_to_book>")
    sys.exit(1)
book_path = sys.argv[1]

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    text = get_book_text(book_path)
    words = book_words(text)
    repeated_count = repeated_char(text)
    char_list = sorted_dict(repeated_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("----------- Character Count ----------")
    for c, count in char_list:
        if c.isalpha() == True:
            print(f"{c}: {count}")

main()