def rock_paper_scissors(first, second):
    if first == second:
        return "Tie"

    if first == "R" and second == "S":
        return "First"
    if first == "S" and second == "P":
        return "First"
    if first == "P" and second == "R":
        return "First"
    return "Second"

    # ADD ADDITIONAL CODE HERE!


print(rock_paper_scissors("R", "R"))  # Tie
print(rock_paper_scissors("R", "S"))  # First
print(rock_paper_scissors("R", "P"))  # Second
print(rock_paper_scissors("S", "S"))  # Tie
print(rock_paper_scissors("S", "P"))  # First
print(rock_paper_scissors("S", "R"))  # Second
print(rock_paper_scissors("P", "P"))  # Tie
print(rock_paper_scissors("P", "R"))  # First
print(rock_paper_scissors("P", "S"))  # Second
