def words_count(book_text):
    num_words = len(book_text.split())
    return num_words

def characters_count(book_text):
    text_lower = book_text.lower()
    nums_char = {}
    for char in set(text_lower):
        nums_char[char] = text_lower.count(char)
    return nums_char

def sort_dict(chars_dict):
    sorted_items = sorted(chars_dict.items(), key = lambda item:item[1], reverse=True)
    sorted_dict = dict(sorted_items)
    return sorted_dict