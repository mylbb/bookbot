import sys
from stats import words_count, characters_count, sort_dict

def get_book_text(path_to_book):
    with open(path_to_book) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_book = sys.argv[1]

    book_text = get_book_text(path_to_book)
    num_words = words_count(book_text)
    #print(f"{num_words} words found in the document")
    num_chars = characters_count(book_text)
    #print(num_chars)

    print("============ BOOKBOT ============")
    print()
    print(f"Analyzing book found at {path_to_book}...")
    print()
    print("----------- Word Count ----------")
    print()
    print(f'Found {num_words} total words')
    print()
    print("--------- Character Count -------")

    sorted_dict = sort_dict(num_chars)
    for key in sorted_dict:
        if key.isalpha():
            print(f'{key}: {sorted_dict[key]}')
    
    print()
    print("============= END ===============")

main()
