import requests

# retrieve the full text of The Importance of Being Earnest
the_url = "http://www.gutenberg.org/cache/epub/844/pg844.txt"
paragraph = str(requests.get(the_url).content)

# run the frequency analysis as before
def count(paragraph):
    lows = "abcdefghijklmnopqrstuvwxyz"
    ups =  "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    number_of_e = 0
    total_chars = 0
    for this_char in paragraph:
        if this_char in lows or this_char in ups:
            total_chars = total_chars + 1
            if this_char == "e":
                number_of_e = number_of_e + 1

    percent_with_e = (number_of_e / total_chars) * 100
    print("Your text contains", total_chars, "alphabetic characters of which", number_of_e, "(", percent_with_e, "%)", "are 'e'.")

count(paragraph)
print(paragraph)