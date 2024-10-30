import numpy as np

class SudokuCSP:
    def __init__(self, grid):
        self.grid = grid

    def is_valid(self, row, col, num):
        # Check if num is in the row
        if num in self.grid[row]:
            return False
        # Check if num is in the column
        if num in [self.grid[i][col] for i in range(9)]:
            return False
        # Check if num is in the 3x3 grid
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if self.grid[start_row + i][start_col + j] == num:
                    return False
        return True

    def find_empty_location(self):
        # Find the first empty cell in the grid
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == 0:
                    return i, j
        return None

    def solve(self):
        empty = self.find_empty_location()
        if not empty:
            return True  # Solution found
        row, col = empty

        # Minimum Remaining Values (MRV) heuristic: Test numbers 1-9
        for num in range(1, 10):
            if self.is_valid(row, col, num):
                self.grid[row][col] = num
                if self.solve():
                    return True
                self.grid[row][col] = 0  # Undo assignment
        return False

    def display(self):
        for row in self.grid:
            print(" ".join(str(num) if num != 0 else '.' for num in row))

# Define an initial unsolved Sudoku puzzle (0 represents an empty cell)
initial_grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Create a Sudoku CSP instance and solve the puzzle
sudoku = SudokuCSP(initial_grid)
print("Initial Sudoku State:")
sudoku.display()

# Solve the puzzle
if sudoku.solve():
    print("\nSolved Sudoku State:")
    sudoku.display()
else:
    print("No solution exists for the given Sudoku puzzle.")
