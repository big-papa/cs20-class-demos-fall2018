def vowel_killer(some_word):
    """Removes all vowels from a string, and returns the result."""
    vowels = "aeiouAEIOU"
    word_without_vowels = ""
    for letter in some_word:
        if letter not in vowels:
            word_without_vowels = word_without_vowels + letter
    return word_without_vowels

def even_letters(word):
    """Returns every other letter from the given word."""
    new_word = ""
    for counter in range(len(word)):
        if counter % 2 == 0:
            new_word = new_word + word[counter]
    return new_word


def aydens_code(word):
    """Flips the alphabet for the given word."""
    flipped_word = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for letter in word:
        location = alphabet.find(letter)
        reversed_location = 25 - location
        flipped_word = flipped_word + alphabet[reversed_location]
    return flipped_word

print(aydens_code("ayden"))
        

