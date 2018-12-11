file_in = open("moby.txt")
text = file_in.read()

def count_letter_frequency(text, letter_to_count):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number_of_es = 0
    total_letters = 0

    for letter in text:
        if letter in alphabet:
            total_letters = total_letters + 1
            if letter.lower() == letter_to_count:
                number_of_es += 1
                
    percent_with_char = number_of_es / total_letters * 100
    percent_with_char = round(percent_with_char, 2)

    #print("The text has", total_letters, "letters in total, and", number_of_es, "of them are e's.")
    print(letter_to_count, percent_with_char)

for this_letter in "abcdefghijklmnopqrstuvwxyz":
    count_letter_frequency(text, this_letter)