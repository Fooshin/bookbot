def book_words(book):
    num_words = 0
    words = book.split()
    for word in words:
        num_words += 1
    return num_words

def repeated_char(book):
    text = book.lower()
    char_dict = {}
    for char in text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sorted_dict(data): 
    sorted_by_count = sorted(data.items(), reverse=True, key=lambda x: x[1])
    return sorted_by_count