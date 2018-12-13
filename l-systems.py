import turtle

def apply_rules(letter):
    """Apply rules to a single letter and return the result."""
    if letter == "F":
        return "F-F++F-F"
    
    #elif letter == "B":
    #    return "AB"
    
    else:
        return letter
    
def process_string(original):
    """Apply the rules to a string, one letter at a time, then return result."""
    transformed_string = ""
    for letter in original:
        transformed_string = transformed_string + apply_rules(letter)
    return transformed_string

def create_l_system(axiom, number_of_iterations):
    """Start with axiom, then transform the string number_of_iteration times."""
    starting_string = axiom
    for counter in range(number_of_iterations):
        ending_string = process_string(starting_string)
        starting_string = ending_string
    return ending_string
    

canvas = turtle.Screen()
ashton = turtle.Turtle()
ashton.penup()
ashton.goto(-550, -400)
ashton.pendown()
ashton.speed(0)

instructions = create_l_system("F", 5)
for task in instructions:
    if task == "F":
        ashton.forward(5)
    elif task == "B":
        ashton.backward(5)
    elif task == "+":
        ashton.right(60)
    elif task == "-":
        ashton.left(60)

#print(create_l_system("A", 11))