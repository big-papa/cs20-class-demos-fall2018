def sum_to(ending_number):
    """Returns the sum of all integers from 1 to ending_number."""
    running_total = 0
    for counter in range(ending_number + 1):
        running_total = running_total + counter

    return running_total

def gauss_sum_to(ending_number):
    """Uses Gaussian formula to find a sum."""
    return ending_number * (ending_number + 1) / 2


##print(sum_to(100))
#print(gauss_sum_to(1000000000))

def square(n):
    """Returns the square of the given number."""
    the_square = 0
    for counter in range(n):
        the_square = the_square + n
    return the_square
    
print(square(5))

