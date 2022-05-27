# ADD FUNCTION HERE!
def quadrant(a, b):
    if a > 0:
        if b > 0:
            return "First Quadrant"
        elif b < 0:
            return "Fourth Quadrant"
        else:
            return "On the Boundary"
    elif a < 0:
        if b > 0:
            return "Second Quadrant"
        elif b < 0:
            return "Third Quadrant"
        else:
            return "On the Boundary"
    else:
        return "On the Boundary"


print(quadrant(10, 5))  # First Quadrant
print(quadrant(-5, 3))  # Second Quadrant
print(quadrant(-5, -7))  # Third Quadrant
print(quadrant(3, -5))  # Fourth Quadrant
print(quadrant(0, -3))  # On the Boundary
