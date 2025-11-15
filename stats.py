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

def get_sorted_dictionary(counts):

    def sort_on(items):
        return items["num"]

    sorted_counts = []
    for key in counts:
        key_value = counts[key]
        sub_directory = {"char": key, "num": key_value}
        sorted_counts.append(sub_directory)
    sorted_counts.sort(reverse=True, key=sort_on)
    return sorted_counts
