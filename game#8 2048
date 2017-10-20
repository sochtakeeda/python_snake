# executable link: http://www.codeskulptor.org/#user43_ZkBnikcTp2_14.py
"""
Clone of 2048 game.
"""

import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def slide(line):
    """
    shifts all non zero elements left
    """
    result = []
    dummy_num = 0
    for dummy_index in range(len(line)):
        result.append(0)
        if line[dummy_index] != 0:
            result[dummy_num] = line[dummy_index]
            dummy_num += 1
    return result            

def merge(line):
    """
    merges a single row or column in 2048.
    """
    result = slide(line)
    for dummy_num in range(len(result)):
        if dummy_num + 1 < len(result):
            if result[dummy_num] == result[dummy_num + 1]:
                result[dummy_num] *= 2
                result[dummy_num + 1] = 0
    return slide(result)
    
        
class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self.gheight = grid_height
        self.gwidth = grid_width
        self.grid = []
        self.reset()

        # computing initial tiles and dictionary
        initial_UP = []
        initial_DOWN = []
        initial_LEFT = []
        initial_RIGHT = []
        initial_UP = self.initial_tiles((0, 0), OFFSETS[LEFT], self.gwidth)
        initial_DOWN = self.initial_tiles((self.gheight - 1, 0), OFFSETS[LEFT], self.gwidth)
        initial_LEFT = self.initial_tiles((0, 0), OFFSETS[UP], self.gheight)
        initial_RIGHT = self.initial_tiles((0, self.gwidth - 1), OFFSETS[UP], self.gheight)
        self.initial_dic = {UP : initial_UP, DOWN : initial_DOWN,
                            LEFT : initial_LEFT, RIGHT : initial_RIGHT} 
    
    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self.grid = [[0 for dummy_col in range(self.gwidth)] for dummy_row in range(self.gheight)]
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        print "grid values:"
        for row in range(self.gheight):
            print self.grid[row]
        return ""
    
    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self.gheight

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self.gwidth

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        self.mov = False
        if direction == UP:
                for dummy_pos in self.initial_dic[UP]:
                    self.mov = self.traverse_grid(dummy_pos, OFFSETS[UP], self.gheight)
        elif direction == DOWN:
                for dummy_pos in self.initial_dic[DOWN]:
                    self.mov = self.traverse_grid(dummy_pos, OFFSETS[DOWN], self.gheight)
        elif direction == LEFT:
                for dummy_pos in self.initial_dic[LEFT]:
                    self.mov = self.traverse_grid(dummy_pos, OFFSETS[LEFT], self.gwidth)
        elif direction == RIGHT:
                for dummy_pos in self.initial_dic[RIGHT]:
                    self.mov = self.traverse_grid(dummy_pos, OFFSETS[RIGHT], self.gwidth)

        if self.mov:
                self.new_tile()
            
            
    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        dummy_rowrange = range(0, self.gheight)
        dummy_colrange = range(0, self.gwidth)
        random.shuffle(dummy_rowrange)
        random.shuffle(dummy_colrange)
        for row in dummy_rowrange:
            for col in dummy_colrange:
                if self.grid[row][col] == 0:
                    self.grid[row][col] = random.choice([2, 2, 2, 2, 2, 2, 2, 2, 2, 4])
                    return []

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self.grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self.grid[row][col]
    
    def initial_tiles(self, start_cell, direction, num_steps):
        """
        creates initial tiles
        """
        dummy_list = []
        for step in range(num_steps):
            row = start_cell[0] + step * direction[0]
            col = start_cell[1] + step * direction[1]
            dummy_list.append((row, col))
        return dummy_list
    
    def traverse_grid(self, start_cell, direction, num_steps):
        """
        Function that iterates through the cells in a grid
        in a linear direction

        Both start_cell is a tuple(row, col) denoting the
        starting cell

        direction is a tuple that contains difference between
        consecutive cells in the traversal
        """
        dummy_list = []
        new_list = []
        for step in range(num_steps):
            dummy_row = start_cell[0] + step * direction[0]
            dummy_col = start_cell[1] + step * direction[1]
            dummy_list.append(self.grid[dummy_row][dummy_col])
        new_list = merge(dummy_list)
        
        for step in range(num_steps):
            dummy_row = start_cell[0] + step * direction[0]
            dummy_col = start_cell[1] + step * direction[1]
            # check to see if anything moves by comparing 
            # updated cells with old cells
            if new_list[step] != self.grid[dummy_row][dummy_col]:
                self.mov = True
            self.grid[dummy_row][dummy_col] = new_list[step]          
        return self.mov

poc_2048_gui.run_gui(TwentyFortyEight(4, 4))



