import easygui_qt as easy

person1 = "Jenna"
person2 = "Therrill"

the_message = f"""<h1>Class List</h1>

<p>The people in our <em>Computer Science 20</em> class includes:</p>

<ul>
    <li>{person1}</li>
    <li>{person2}</li>
    <li>Ashton</li>
    <li>Josiah</li>
    <li>Agnes</li>
</ul>"""

easy.show_message(the_message)
