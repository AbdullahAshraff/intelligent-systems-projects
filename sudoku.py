class SudokuCSP:
    def __init__(self, grid):
        self.grid = grid

    def is_valid(self, row, col, num):
        if num in self.grid[row]:  # if exists in the same row
            return False
        if num in [self.grid[i][col] for i in range(9)]:  # if exists in the same column
            return False

        # if exists in the 3x3 grid
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col+ 3):
                if self.grid[i][j] == num:
                    return False
        return True

    def find_empty_location(self):
        """
        Returns tuple (row, col) of the first empty cell in the grid.
        """
        # Find the first empty cell in the grid
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == 0:
                    return i, j
        return None

    def solve(self):
        """
        Returns True if a solution is found, False otherwise.
        """
        empty_pos = self.find_empty_location()
        if not empty_pos:
            return True  # Solution found
        row, col = empty_pos

        # Minimum Remaining Values (MRV) heuristic: Test numbers 1-9
        for num in range(1, 10):
            if self.is_valid(row, col, num):
                self.grid[row][col] = num
                if self.solve():
                    return True
                self.grid[row][col] = 0  # Undo assignment
        return False

    def display(self):
        for i, row in enumerate(self.grid):
            if i % 3 == 0 and i != 0:
                print("------------------------")

            for j, num in enumerate(row):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")

                if j == 8:
                    print(num if num != 0 else ". ")
                else:
                    print(f"{num} " if num != 0 else ". ", end="")


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
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]

sudoku = SudokuCSP(initial_grid)
print("Initial Sudoku State:")
sudoku.display()

if sudoku.solve():
    print("\nSolved Sudoku State:")
    sudoku.display()
else:
    print("No solution exists for the given Sudoku puzzle.")
