import scrabble 

letters = "abcdefghijklmnopqrstufwxyz"
vowels = "aeiou"

def has_a_double(letter):
    for word in scrabble.wordlist:
        if letter + letter in word:
           return True
    return False

def has_all_vowels(word):
    for vowel in vowels:
        if vowel not in word:
            return False
    return True

for letter in letters:
    if not has_a_double(letter):
        print(letter + " never appears doubled")

counter = 0
for word in scrabble.wordlist:
    if has_all_vowels(word):
        counter += 1 
print (str(counter) + " words have all the vowels")
