alphabet = "abcdefghijklmnopqrstuvwxyz"
cipher =   "zktmqurejyxwaovcbsgnpdilhf"

message = "hello, how was your day?"
encrypted_message = ""

for letter in message:
    location = alphabet.find(letter)
    if location != -1:
        new_character = cipher[location]
    else:
        new_character = letter
    encrypted_message = encrypted_message + new_character

print(encrypted_message)