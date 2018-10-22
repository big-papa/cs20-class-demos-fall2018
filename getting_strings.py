import easygui_qt as easy

first_name = easy.get_string("Please enter your first name")
last_name = easy.get_string("Please enter your last name")

greeting = "Hello there, " + first_name + " " + last_name + "!"
easy.show_message(greeting)