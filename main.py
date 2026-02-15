from stats import get_num_words, get_num_characters, list_of_dicts
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_file = sys.argv[1]
    text = get_book_text(path_to_file)
    num_words = get_num_words(text)
    num_chars = get_num_characters(text)
    report = list_of_dicts(num_chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in report:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
        else:
            continue
    print("============= END ===============")
    
    
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()
    
main()