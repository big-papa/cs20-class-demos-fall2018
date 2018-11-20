def is_even(some_number):
    if some_number % 2 == 0:
        return True
    else:
        return False
    
def is_odd(number):
    return not is_even(number)


print(is_odd(7))