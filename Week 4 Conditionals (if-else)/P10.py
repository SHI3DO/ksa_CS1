def better(gold1, silver1, bronze1, gold2, silver2, bronze2):
    if gold1 > gold2:
        return "First"
    if gold1 < gold2:
        return "Second"
    if silver1 > silver2:
        return "First"
    if silver1 < silver2:
        return "Second"
    if bronze1 > bronze2:
        return "First"
    if bronze1 < bronze2:
        return "Second"
    return "Tie"

    # ADD ADDITIONAL CODE HERE!


print(better(10, 4, 24, 1, 35, 25))  # First
print(better(1, 35, 25, 10, 4, 24))  # Second
print(better(10, 18, 0, 10, 4, 24))  # First
print(better(10, 4, 24, 10, 18, 0))  # Second
print(better(10, 20, 5, 10, 20, 4))  # First
print(better(10, 20, 4, 10, 20, 5))  # Second
print(better(10, 20, 5, 10, 20, 5))  # Tie
