def square(original_number):
    """Returns the square of the given number."""
    running_total = 0
    for counter in range(original_number):
        running_total = running_total + original_number
    return running_total


def sum_to(n):
    """Adds up all the numbers from 1 to the given n, and returns the sum."""
    the_sum = 0
    for counter in range(n+1):
        the_sum = the_sum + counter
    return the_sum

def gauss_sum_to(n):
    """Finds the sum, using Gauss' formula."""
    the_sum = n * (n + 1) / 2
    return the_sum
    
print(gauss_sum_to(1000000000000))