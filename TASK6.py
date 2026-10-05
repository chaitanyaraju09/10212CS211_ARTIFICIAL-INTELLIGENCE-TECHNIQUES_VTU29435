# University Campus Map Coloring using CSP Backtracking

zones = ["A", "B", "C", "D", "E"]
colors = ["Red", "Green", "Blue", "Yellow"]

adjacent = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D", "E"],
    "D": ["B", "C", "E"],
    "E": ["C", "D"]
}

assignment = {}

def is_safe(zone, color):
    """Check that zone has a different color from its neighbors."""
    for neighbor in adjacent[zone]:
        if assignment.get(neighbor) == color:
            return False
    return True

def solve(index=0):
    """Solve the CSP using backtracking."""
    if index == len(zones):
        return True

    zone = zones[index]

    for color in colors:
        if is_safe(zone, color):
            assignment[zone] = color

            if solve(index + 1):
                return True

            del assignment[zone]  # Backtrack

    return False

if solve():
    print("Valid Campus Map Coloring:")
    for zone in zones:
        print(f"{zone} = {assignment[zone]}")
else:
    print("No valid coloring exists.")


#   _____OUTPUT_____


#Valid Campus Map Coloring:
#A = Red
#B = Green
#C = Blue
#D = Red
#E = Green
