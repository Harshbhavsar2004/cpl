"""
Problem: Minesweeper Grid Generator
Given a grid size and bomb positions, generate a Minesweeper grid where each cell contains the number of bombs in adjacent cells (including diagonals), or 'B' if it is a bomb.

Input:
- Level (1: 5x5, 2: 7x7, 3: 9x9)
- Bomb positions as (x, y) pairs, entered by the user, until 'done' is typed.

Output:
- The Minesweeper grid with numbers and 'B' for bombs.

Sample Input:
1
0,0
1,1
done

Sample Output:
B 2 0 0 0
2 B 1 0 0
0 1 1 0 0
0 0 0 0 0
0 0 0 0 0

Explanation:
Bombs are placed at (0,0) and (1,1). Each cell shows the number of adjacent bombs, or 'B' if it is a bomb.

Time Complexity: O(n^2), where n is the grid size.
Space Complexity: O(n^2), for the grid.
"""

def create_grid(level):
    if level == 1:
        size = 5
    elif level == 2:
        size = 7
    elif level == 3:
        size = 9
    else:
        print("Invalid level")
        return
    grid = [[0 for _ in range(size)] for _ in range(size)]
    return grid, size


def is_valid(x, y, size):
    return 0 <= x < size and 0 <= y < size


def place_bombs(grid, size, bomb_positions):
    for (x, y) in bomb_positions:
        grid[x][y] = -1
    for x in range(size):
        for y in range(size):
            if grid[x][y] == -1:
                continue
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    nx, ny = x + dx, y + dy
                    if is_valid(nx, ny, size) and grid[nx][ny] == -1:
                        grid[x][y] += 1


def print_grid(grid):
    for row in grid:
        print(" ".join(str(cell) if cell != -1 else "B" for cell in row))


def main():
    print("Select level:")
    print("1. Easy (5x5)")
    print("2. Medium (7x7)")
    print("3. Hard (9x9)")
    level = int(input("Enter level (1, 2, or 3): "))
    grid, size = create_grid(level)

    bomb_positions = []
    print("Enter bomb positions in format (x, y). Type 'done' to stop.")

    while True:
        position = input("Enter bomb position (x, y): ")
        if position.lower() == 'done':
            break
        try:
            x, y = map(int, position.split(","))
            if is_valid(x, y, size):
                bomb_positions.append((x, y))
            else:
                print("Invalid position. Try again.")
        except ValueError:
            print("Invalid input. Enter coordinates in the form of x,y.")
    place_bombs(grid, size, bomb_positions)
    print("Minesweeper Grid:")
    print_grid(grid)


if __name__ == "__main__":
    main()
 