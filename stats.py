def get_num_words(text):
    split_text = text.split()
    return len(split_text)
    
def get_num_characters(text):
    result = {}
    for char in text.lower():
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result

def target_word_search(text, target_word):
    split_text = text.split()
    counter = 0
    for word in split_text:
        if word.strip("!“.,;:'\"()[]{}").lower() == target_word.lower():
            counter += 1
    return counter

def sort_on(item):
    return item['num']

def character_dictionary(result):
    char_dict = []
    for key, value in result.items():
        char_dict.append({'char': key, 'num': value})
    char_dict.sort(key=sort_on, reverse=True)
    return char_dict

def word_dictionary(text):
    word_dict = {}
    split_text = text.split()
    for word in split_text:
        cleaned_word = word.strip("“!.,;:'\"()[]{}").lower()
        if cleaned_word in word_dict:
            word_dict[cleaned_word] += 1
        else:
            word_dict[cleaned_word] = 1
    return word_dict

def most_common_words(text, stopwords, n=10):
    word_list = []
    word_dict = word_dictionary(text)
    for key, value in word_dict.items():
        if len(key) > 1 and key not in stopwords:
            word_list.append({'word': key, 'num': value})
    word_list.sort(key=sort_on, reverse=True)
    return word_list[:n]

def target_word_in_sentence(text, target_word, n=8):
    text = text.replace('?', '.').replace('!', '.')
    sentences = text.split(".")
    sentences_list = []
    for sentence in sentences:
        sentence = sentence.replace('\n', ' ').strip().lstrip('"” ')
        if target_word.lower() in sentence.lower() and sentence:
            sentences_list.append(sentence)
            if len(sentences_list) >= n:
                break
            
    return sentences_list