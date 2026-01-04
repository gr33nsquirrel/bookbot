# Import modules
from stats import get_word_count, get_char_count, sort_book


# Define main
def main():
    book_path = "books/frankenstein.txt"                    # Book filepath 
    text = get_book_text(book_path)                         # Read book file
    word_count = get_word_count(text)                       # Get word count
    char_count = get_char_count(text)                       # Get character count
    book_report = sort_book(char_count)                     # Sort character count
    print("============ BOOKBOT ============")              # Start report
    print(f"Analyzing book found at {book_path} ...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    for x in book_report:
        print(f"{x['char']}: {x['num']}")
    
    print("============= END ===============")              # End report
    

# Read book file
def get_book_text(path):
    with open(path) as f:
        return f.read()


# Call main
main()