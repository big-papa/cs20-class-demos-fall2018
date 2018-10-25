import easygui_qt as easy

my_message = """
<h1>Some Title</h1>
<p>Stuff I want to say...</p>
<ul>
    <li>Thing 1</li>
    <li>Thing 2</li>
</ul>"""

easy.show_html("Demo", my_message)