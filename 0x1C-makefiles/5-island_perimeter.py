#!/usr/bin/python3

def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in the grid.

    Args:
    grid (List[List[int]]): A list of list of integers representing the island.

    Returns:
    int: The perimeter of the island.
    """
    rows = len(grid)
    if rows == 0:
        return 0

    cols = len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4  # Start with the maximum perimeter

                # Check left neighbor
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2  # Deduct 2 for shared edge

                # Check top neighbor
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2  # Deduct 2 for shared edge

    return perimeter

# Example usage
grid = [
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0]
]
perimeter = island_perimeter(grid)
print("Perimeter of the island:", perimeter)
