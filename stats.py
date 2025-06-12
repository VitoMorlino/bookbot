def get_num_words(text):
    wordlist = text.split()
    return len(wordlist)


def count_each_character(text):
    counted_chars = {}
    lowertext = text.lower()

    for char in lowertext:
        if char in counted_chars:
            # increment the count value
            counted_chars[char] += 1
        else:
            # add it to the dictionary with value 1
            counted_chars[char] = 1

    return counted_chars


def sort_on(d):
    return d["num"]


def sort_dictionary(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
