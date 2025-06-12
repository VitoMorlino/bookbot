def get_book_text(filepath):
    contents = ""
    with open(filepath) as file:
        contents = file.read()
    return contents


def get_num_words(text):
    wordlist = text.split()
    return len(wordlist)


def main():
    num_words = get_num_words(get_book_text("./books/frankenstein.txt"))
    print(f"{num_words} words found in the document")


main()
