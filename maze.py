import random
import time
import tkinter as tk

CELL_SIZE = 40



def create_maze():
    return [
        ['S', 0,   1,   0],
        [1,   0,   1,   0],
        [0,   0,   0,   1],
        [0,   1,   0,  'G']
    ]


def generate_maze(rows, cols):
    maze = [[0 if random.random() > 0.3 else 1 for _ in range(cols)] for _ in range(rows)]
    maze[0][0] = 'S'
    maze[rows-1][cols-1] = 'G'
    return maze


