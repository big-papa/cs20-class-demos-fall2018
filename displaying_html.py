import easygui_qt as easy

your_fav = easy.get_string("What's your favourite NBA team?")

best_teams = f"""<h1>Best NBA Teams</h1>

<p>The <em>best teams</em> in the NBA are:</p>

<ul>
    <li>Spurs</li>
    <li>Warriors</li>
    <li>Celtics</li>
    <li>Raptors</li>
    <li>{your_fav}</li>
</ul>"""

easy.show_message(best_teams)