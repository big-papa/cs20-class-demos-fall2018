def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
    
def is_odd(some_number):
    return not is_even(some_number)

print( is_odd(9) )