def vowel_killer(some_word):
    """Removes all vowels from a string, and returns the result."""
    vowels = "aeiouAEIOU"
    word_without_vowels = ""
    for letter in some_word:
        if letter not in vowels:
            word_without_vowels = word_without_vowels + letter
    return word_without_vowels

print(vowel_killer("Saskatoon"))