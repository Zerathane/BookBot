from stats import *
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

def get_stopwords(path_to_stopwords_file):
    with open("stopwords.txt") as f:
        stopwords = f.read().split()
    return set(stopwords)


def print_report(path_to_file,num_words, num_chars, num_target_word, target_word, report, most_common_wrd, target_word_sentences):
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
    for _ in range(4):
        time.sleep(0.7)
        print(".", end="", flush=True)
    print(f"Analyzing book found at {path_to_file}")
    time.sleep(1)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    if num_target_word:
        print("-------- Target Word Count ------")
        time.sleep(1)
        print(f"The word '{target_word}' was found {num_target_word} times in the text.")
        print("---------------------------------")
        print(f"The word '{target_word}' appears in the following sentences:")
        print("---------------------------------")
        time.sleep(1)
        for sentence in target_word_sentences:
            print(f"  - {sentence}")
    time.sleep(1)
    print("------- most common words -------")
    for item in most_common_wrd:
        print(f"{item["word"]}: {item["num"]}")
    time.sleep(1)
    print("--------- Character Count -------")
    for item in report:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
        else:
            continue
    print("============= END ===============")


def main():
    path_to_file, target_word = get_arguments()
    text = get_book_text(path_to_file)
    num_words = get_num_words(text)
    num_chars = get_num_characters(text)
    stopwords = get_stopwords("stopwords.txt")
    most_common_wrd = most_common_words(text, stopwords, n=10)
    if target_word:
        num_target_word = target_word_search(text, target_word)
        target_word_sentences = target_word_in_sentence(text, target_word)
    else: 
        num_target_word = None
        target_word_sentences = None
    report = character_dictionary(num_chars)
    print_report(path_to_file, num_words, num_chars, num_target_word, target_word, report, most_common_wrd, target_word_sentences)

main()