import easygui_qt as easy

first_name = easy.get_string("Please enter your first name")
last_name = easy.get_string("Please enter your last name")
age = easy.get_integer("Please enter your age")

greeting = "Hi there, " + first_name + " " + last_name +"! You are already " + str(age) + " years old."
easy.show_message(greeting)

