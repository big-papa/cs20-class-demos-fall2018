def cube(some_number):
    """Returns the cube of any number."""
    the_answer = some_number * some_number * some_number
    return the_answer
    
my_number = int(input("Please enter a number to cube: "))
my_answer = cube(my_number)
print("The cube of", my_number, "is", my_answer)