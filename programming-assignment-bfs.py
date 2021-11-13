# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 07:54:11 2021

@author: Tashfeen Mustafa Choudhury

Implementing Breadth First Search and A* search in a maze
"""

import time

class Maze(object):
    """A pathfinding problem."""

    def __init__(self, grid, location):
        """Instances differ by their current agent locations."""
        self.grid = grid
        self.location = location
    
    def display(self):
        """Print the maze, marking the current agent location."""
        for r in range(len(self.grid)):
            for c in range(len(self.grid[r])):
                if (r, c) == self.location:
                    print('*', end='')
                else:
                    print(self.grid[r][c], end='')
            print()

    def moves(self):
        """
            Return a list of possible moves given the current agent location.
            Represent graph as a hashtable using dictionary
            example: 
                possible_moves = [(1, 2), (2, 1)]
        """
        # YOU FILL THIS IN
        possible_moves = []

        current_location = self.location 
        
        (r, c) = current_location
        # check if location above the current location is empty
        # if so, add the location as neighbor of current node
        if self.grid[r - 1][c] != 'X':
            # add (r - 1, c) as neighbor
            possible_moves.append((r - 1, c))
            
        # check if location right of current location is empty
        # if so, add the location as neighbor of current node
        if self.grid[r][c + 1] != 'X':
            possible_moves.append((r, c + 1))
        # check if location left of current location is empty
        # if so, add the location as neighbor of current node
        if self.grid[r][c - 1] != 'X':
            possible_moves.append((r, c - 1))
        # check if location below the current location is empty
        # if so, add the location as neighbor of current node
        if self.grid[r + 1][c] != 'X':
            possible_moves.append((r + 1, c))
            
        return possible_moves
    
    def neighbor(self, move):
        """
            Return another Maze instance with a move made.
        """
        # YOU FILL THIS IN
        (r, c) = move
        return Maze(self.grid, (r, c))

class Agent(object):
    """Knows how to find the exit to a maze with BFS."""
    def __init__(self):
        self.frontier = []
        self.visited_nodes = []
        
    def bfs(self, maze, goal):
        """
            Return an ordered list of moves to get the maze to match the goal.
        """
        # YOU FILL THIS IN
        self.frontier.append([maze.location])
        
        while self.frontier:
            path = self.frontier.pop(0)
            if not path[-1] in self.visited_nodes:
                if path[-1] == goal.location:
                    return path
                else:
                    maze = Maze(maze.grid, path[-1])
                    moves = maze.moves()
                    
                    for move in moves:
                        new_path = path.copy()
                        new_path.append(move)
                        self.frontier.append(new_path)
                        new_path = []
                    self.visited_nodes.append(path[-1])
        return None
                

def main():
    """Create a maze, solve it with BFS, and console-animate."""
    
    grid = ["XXXXXXXXXXXXXXXXXXXX",
            "X     X    X       X",
            "X XXXXX XXXX XXX XXX",
            "X       X      X X X",
            "X X XXX XXXXXX X X X",
            "X X   X        X X X",
            "X XXX XXXXXX XXXXX X",
            "X XXX    X X X     X",
            "X    XXX       XXXXX",
            "XXXXX   XXXXXX     X",
            "X   XXX X X    X X X",
            "XXX XXX X X XXXX X X",
            "X     X X   XX X X X",
            "XXXXX     XXXX X XXX",
            "X     X XXX    X   X",
            "X XXXXX X XXXX XXX X",
            "X X     X  X X     X",
            "X X XXXXXX X XXXXX X",
            "X X                X",
            "XXXXXXXXXXXXXXXXXX X"]

    maze = Maze(grid, (1,1))
    maze.display()
    
    agent = Agent()
    goal = Maze(grid, (19,18))
    path = agent.bfs(maze, goal)

    while path:
        move = path.pop(0)
        maze = maze.neighbor(move)
        time.sleep(0.25)
        maze.display()

if __name__ == '__main__':
    main()