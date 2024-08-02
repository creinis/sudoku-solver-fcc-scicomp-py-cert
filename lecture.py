# Sudoku Solver

# Step 1

# In this project, you will learn about classes and objects by building a sudoku puzzle solver.

# In Python, a class is a blueprint for creating objects. 
# Objects created from a class are instances of that class. You can create a class using this syntax:

# class ClassName:

# First, you will create a 9x9 board by using classes and then populate it with the puzzle values.

# Begin by creating a Board class.

class Board:

# Step 2

# A new instance of a class is created by using the function notation: ClassName(). 
# The instantiation creates an empty object. 
# Classes can have methods, which are like local functions for each instance. 
# Methods are declared as follows:

# class ClassName:
    def method_name():
        pass

# The __init__ method is a special method that allows you to instantiate an object to a customized state. 
# When a class implements an __init__ method, __init__ is automatically called upon instantiation.

# Create an __init__ method inside your Board class.

    def __init__():
        pass

# Step 3

# Add two parameters to the __init__ method, order matters:

#    self: This is a reference to the instance of the class. It is a convention to name this parameter self.
#    board: The board parameter is expected to be passed when creating an instance of the Board class.

# Step 4

# Inside the __init__ method, assign the value of the board parameter (which is passed when creating an 
# instance of the Board class) to an instance variable named board using self.board.

# self.board refers to the board attribute of the instance of the class. 
# It's a variable that belongs to the object created from the Board class.

    def __init__(self, board):
        self.board = board

# Step 5

# Now you will move to the actual construction of the board, which is a 9x9 gird.

# The input puzzle would look like this:

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

# The resulting grid would look like this:

# Define a method __str__ within the Board class. Also, add the self parameter. 
# This method is automatically called when you use the str() function on an instance of the class or when 
# you use print() with the object.

def __str__(self):
    pass














