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
    maze = [[1 for _ in range(cols)] for _ in range(rows)]

    
    x, y = 0, 0
    maze[x][y] = 0

    while (x, y) != (rows - 1, cols - 1):
        if (x < rows - 1) and (y < cols - 1):
            if random.random() < 0.5:
                x += 1
            else:
                y += 1
        elif x < rows - 1:
            x += 1
        else:
            y += 1

        maze[x][y] = 0

    
    for i in range(rows):
        for j in range(cols):
            if random.random() < 0.25:
                maze[i][j] = 0

    maze[0][0] = 'S'
    maze[rows - 1][cols - 1] = 'G'

    return maze


def get_start_goal(maze):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'S':
                start = (i, j)
            if maze[i][j] == 'G':
                goal = (i, j)
    return start, goal

def get_neighbors(maze, x, y):
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    neighbors = []

    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]):
            if maze[nx][ny] != 1:
                neighbors.append((nx, ny))

    return neighbors