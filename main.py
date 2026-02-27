from stats import get_num_words, get_num_characters, list_of_dicts, target_word_search
import sys
import time


def get_arguments():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book> <target_word (optional)>")
        sys.exit(1)
    path_to_file = sys.argv[1]
    target_word = None
    if len(sys.argv) >= 3:
        target_word = sys.argv[2]
    return path_to_file, target_word


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()


def print_report(path_to_file,num_words, num_chars, num_target_word, target_word, report):
    print("==============================================================")
    print("  ██████╗  ██████╗  ██████╗ ██╗  ██╗██████╗  ██████╗ ████████╗")
    print("  ██╔══██╗██╔═══██╗██╔═══██╗██║ ██╔╝██╔══██╗██╔═══██╗╚══██╔══╝")
    print("  ██████╔╝██║   ██║██║   ██║█████╔╝ ██████╔╝██║   ██║   ██║   ")
    print("  ██╔══██╗██║   ██║██║   ██║██╔═██╗ ██╔══██╗██║   ██║   ██║   ")
    print("  ██████╔╝╚██████╔╝╚██████╔╝██║  ██╗██████╔╝╚██████╔╝   ██║   ")
    print("  ╚═════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝  ╚═════╝   ╚═╝   ")
    print("==============================================================")
    time.sleep(0.5)
    print("Loading..", end="", flush=True)
    for _ in range(5):
        time.sleep(0.7)
        print(".", end="", flush=True)
    print(f"Analyzing book found at {path_to_file}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    if num_target_word:
        print("-------- Target Word Count ------")
        print(f"Found {num_target_word} occurrences of the word '{target_word}'")
    print("--------- Character Count -------")
    for item in report:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
        else:
            continue
    print("============= END ===============")


def main():
    path_to_file, target_word = get_arguments()
    text = get_book_text(path_to_file)
    num_words = get_num_words(text)
    num_chars = get_num_characters(text)
    if target_word:
        num_target_word = target_word_search(text, target_word)
    else: 
        num_target_word = None
    report = list_of_dicts(num_chars)
    print_report(path_to_file, num_words, num_chars, num_target_word, target_word, report)


main()