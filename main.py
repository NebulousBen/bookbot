def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    # after this it does not work
    num_char = get_num_char(text)
    print(f"{num_char} characters found in document")

def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_num_words(text):
    words = text.split()
    return len(words)




def get_num_char(text):
    """
    Count Characters
    Add a new function to your script that takes the text from the book as a string, and returns the number of times each character appears in the string. Convert any character to lowercase, we don't want duplicates.

    Hints
    I'd recommend using a dictionary of String -> Integer.

    When you print out the dictionary it should look something like this:

    {'p': 6121, 'r': 20818, 'o': 25225, ...
    To convert a string to lowercase use the .lower() method:

    my_string = "FOR FRODO"
    lowered_string = my_string.lower()
    print(lowered_string)
    # for frodo
    
    """
    letter_dict = {}
    lowered_text = text.lower()
    for char in lowered_text:
        letter_dict.append(char)
    


main()
