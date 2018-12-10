def remove_vowels(some_word):
    """Removes all vowels from a string, and returns the result."""
    new_word = ""
    vowels = "aeiouAEIOU"
    for letter in some_word:
        if letter not in vowels:
            new_word = new_word + letter
    return new_word


print(remove_vowels("Saskatoon"))