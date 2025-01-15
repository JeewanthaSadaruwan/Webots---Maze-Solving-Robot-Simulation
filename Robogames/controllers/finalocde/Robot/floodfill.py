# Initialize a 10x10 grid with coordinates
rows, cols = 10, 10
maze_coordinates = [[(i, j) for j in range(cols)] for i in range(rows)]

# Print the grid with coordinates
for row in maze_coordinates:
    print(row)