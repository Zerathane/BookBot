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

def sort_on(list_dicts):
    return list_dicts['num']

def list_of_dicts(result):
    list_dicts = []
    for key, value in result.items():
        list_dicts.append({'char': key, 'num': value})
    list_dicts.sort(key=sort_on, reverse=True)
    return list_dicts



