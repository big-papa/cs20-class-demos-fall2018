import easygui_qt as easy

courses = ["Science", "Math", "Computer Science", "Law", "SPED", "Accounting", "History", "Mechanics", "Photography", "French"]

fav = easy.get_choice("Which course is the best?", "Pick Course", courses)

if fav == "Mechanics":
    easy.show_message("Hey, can you help me with my car?")
elif fav == "Computer Science":
    easy.show_message("Are you just being nice?")
else:
    easy.show_message("Nice! I like " + fav + " too!")
