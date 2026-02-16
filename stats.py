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
        if word.lower() == target_word.lower():
            counter += 1
    return counter

def sort_on(list_dicts):
    return list_dicts['num']

def list_of_dicts(result):
    list_dicts = []
    for key, value in result.items():
        list_dicts.append({'char': key, 'num': value})
    list_dicts.sort(key=sort_on, reverse=True)
    return list_dicts



