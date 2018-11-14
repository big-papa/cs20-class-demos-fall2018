def quadratic_function(a, b, c):
    """Gives you the roots of a quadratic."""
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return "No Real Roots Exist"
    elif discriminant == 0:
        single_root = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
        return single_root
    else:
        first_root = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
        second_root = (-b - (b**2 - 4*a*c)**0.5) / (2*a)
        return [first_root, second_root]

print(quadratic_function(-1, 2, 4))