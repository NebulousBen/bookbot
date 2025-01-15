def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    num_char = get_num_char(text)
    print(num_char)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_char(text):
    letter_dict = {}
    lowered_text = text.lower()
    for char in lowered_text:
        letter_dict.append(char)
    


main()
