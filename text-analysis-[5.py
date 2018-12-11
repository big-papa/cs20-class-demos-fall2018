file_in = open("war.txt")
text = file_in.read()

def frequency_counter(text, letter_to_look_for):
    total_count = 0
    letter_counter = 0
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for letter in text:
        if letter in alphabet:
            total_count = total_count + 1
            if letter.lower() == letter_to_look_for:
                letter_counter = letter_counter + 1

    percentage = round((letter_counter / total_count * 100), 2)
    print(letter_to_look_for, percentage)

for letter in "abcdefghijklmnopqrstuvwxyz":
    frequency_counter(text, letter)