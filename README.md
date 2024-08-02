# Sudoku Solver

###### Technologies:
<p align="center">
<img src="https://img.icons8.com/color/75/000000/python.png" width="75" height="75" alt="Python" style="margin: 10px 15px 0 15px;" />
</p>

### Try it!

To run the Sudoku Solver application, follow the instructions in the Setup section below.

## Project Structure

- `sudoku_solver.py`: Contains the implementation of the Sudoku Solver class and functions.

## Setup

### Prerequisites

- Python 3 installed

### Installation Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/creinis/sudoku-solver-fcc-scicomp-py-cert.git
   cd sudoku-solver-fcc-scicomp-py-cert
   ```

2. Run the Sudoku Solver script:
   ```bash
   python3 sudoku_solver.py
   ```

## Sudoku Solver

### Functionality

The Sudoku Solver is a program that solves a given Sudoku puzzle using a backtracking algorithm. It recursively attempts to place numbers in empty cells, checking if the placement is valid according to Sudoku rules, and backtracks if a number placement leads to a contradiction.

### Practical Use Case

The Sudoku Solver can be used to solve Sudoku puzzles of varying difficulty, providing instant solutions. It is useful for generating solved Sudoku puzzles, validating solutions, or providing hints for players.

### Benefits

- **Efficiency:** Solves Sudoku puzzles quickly using a backtracking algorithm.
- **Validation:** Ensures that the solution adheres to Sudoku rules.
- **Python Standard Library:** Utilizes Python’s built-in data structures for implementation.

## How to Use

1. Run the `sudoku_solver.py` script:
   ```bash
   python3 sudoku_solver.py
   ```

2. The `solve_sudoku` function can be used to solve any 9x9 Sudoku puzzle represented as a 2D list.

### Example Usage

```python
from sudoku_solver import solve_sudoku

# Define the Sudoku puzzle to be solved (0 represents empty cells)
puzzle = [
  [0, 0, 2, 0, 0, 8, 0, 0, 0],
  [0, 0, 0, 0, 0, 3, 7, 6, 2],
  [4, 3, 0, 0, 0, 0, 8, 0, 0],
  [0, 5, 0, 0, 3, 0, 0, 9, 0],
  [0, 4, 0, 0, 0, 0, 0, 2, 6],
  [0, 0, 0, 4, 6, 7, 0, 0, 0],
  [0, 8, 6, 7, 0, 4, 0, 0, 0],
  [0, 0, 0, 5, 1, 9, 0, 0, 8],
  [1, 7, 0, 0, 0, 6, 0, 0, 5]
]

solve_sudoku(puzzle)
```

### Example Output

```plaintext
Puzzle to solve:

╔═══╤═══╤═══╦═══╤═══╤═══╦═══╤═══╤═══╗
║   |   | 2 ║   |   | 8 ║   |   |   ║
╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
║   |   |   ║   |   | 3 ║ 7 | 6 | 2 ║
╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
║ 4 | 3 |   ║   |   |   ║ 8 |   |   ║
╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣
║   | 5 |   ║   | 3 |   ║   | 9 |   ║
╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
║   | 4 |   ║   |   |   ║   | 2 | 6 ║
╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
║   |   |   ║ 4 | 6 | 7 ║   |   |   ║
╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣
║   | 8 | 6 ║ 7 |   | 4 ║   |   |   ║
╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
║   |   |   ║ 5 | 1 | 9 ║   |   | 8 ║
╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
║ 1 | 7 |   ║   |   | 6 ║   |   | 5 ║
╚═══╧═══╧═══╩═══╧═══╧═══╩═══╧═══╧═══╝


Solved puzzle:

╔═══╤═══╤═══╦═══╤═══╤═══╦═══╤═══╤═══╗
║ 9 | 6 | 2 ║ 1 | 7 | 8 ║ 3 | 5 | 4 ║
╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
║ 8 | 1 | 5 ║ 9 | 4 | 3 ║ 7 | 6 | 2 ║
╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
║ 4 | 3 | 7 ║ 6 | 5 | 2 ║ 8 | 1 | 9 ║
╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣
║ 6 | 5 | 8 ║ 2 | 3 | 1 ║ 4 | 9 | 7 ║
╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
║ 7 | 4 | 3 ║ 8 | 9 | 5 ║ 1 | 2 | 6 ║
╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
║ 2 | 9 | 1 ║ 4 | 6 | 7 ║ 5 | 8 | 3 ║
╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣
║ 5 | 8 | 6 ║ 7 | 2 | 4 ║ 9 | 3 | 1 ║
╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
║ 3 | 2 | 4 ║ 5 | 1 | 9 ║ 6 | 7 | 8 ║
╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
║ 1 | 7 | 9 ║ 3 | 8 | 6 ║ 2 | 4 | 5 ║
╚═══╧═══╧═══╩═══╧═══╧═══╩═══╧═══╧═══╝
```

## Function Parameters

- `board`: A

 2D list representing the Sudoku puzzle to be solved, where empty cells are represented by 0.

### Constraints

- The board must be a 9x9 grid with values ranging from 0 to 9, where 0 represents an empty cell.

### Additional Information

- **Solver:** Uses a backtracking algorithm to solve the puzzle.
- **Validation:** Checks if placing a number is valid according to Sudoku rules (row, column, and 3x3 square constraints).
- **Board Representation:** Provides a visually appealing representation of the Sudoku board.

---
#### This is a FreeCodeCamp Challenge for Scientific Computing with Python Projects Certification.
<p align="center">
<img src="https://cdn.freecodecamp.org/platform/universal/fcc_primary.svg" width="250" height="75" alt="freeCodeCamp" style="margin: 0 15px; opacity: 0.6" />
</p>
