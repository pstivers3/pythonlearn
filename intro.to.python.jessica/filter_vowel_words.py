names = ["Alice", "Bob", "Cara", "Dan", "Edith" ]

def starts_with_a_vowel(word):
    return word[0] in "AEIOUaeiou"

def filter_vowel_words(word_list):
    vowel_words = []
    for word in word_list:
        if starts_with_a_vowel(word):
            vowel_words.append(word)
    return vowel_words

print(filter_vowel_words(names))

