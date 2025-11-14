def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_characters(text):
    char_counts = {}
    text_list = list(text)
    for character in text_list:
        lowered_char = character.lower()

        if lowered_char in char_counts:
                char_counts[lowered_char] += 1
        else:
                char_counts[lowered_char] = 1

    return char_counts
