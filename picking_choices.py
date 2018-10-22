import easygui_qt as easy

subjects = ["Computer Science", "Math", "Health Science", "SPED", "Spanish", "Pysch", "History"]

favourite = easy.get_choice("Which subject is your favourite?", "Subject Picker", subjects)

easy.show_message("I like " + favourite + " too!")