# Calculate word count

def get_word_count(book):
    return len(book.split())


# Create dictionary of character counts 

def get_char_count(book):
    char_count = {}

    for c in book.lower():
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1
    
    return char_count


# Sort dictionary by number of characters

def sort_on_count(char_count):
    return char_count["num"]

def sort_book(report):
    book_report = []
    for c in report:
       count = report[c]
       book_report.append({"char": c, "num": count})
    
    book_report.sort(reverse=True,key=sort_on_count)
    return book_report