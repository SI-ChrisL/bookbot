from stats import get_num_words, get_num_characters, get_sorted_dictionary

def main():
        book_path = "books/frankenstein.txt"
        text = get_book_text(book_path)
        num_words = get_num_words(text)
        num_chars = get_num_characters(text)
        # print(f"Found {num_words} total words")
        # print(num_chars)
        output = get_sorted_dictionary(num_chars)
        print(output)

def get_book_text(path):
        with open(path) as file:
                return file.read()

main()