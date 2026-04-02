import time
from utils import draw_maze

import time
from utils import draw_maze

def get_neighbors(maze, x, y):
    neighbors = []
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]):
            if maze[nx][ny] != 1:
                neighbors.append((nx, ny))

    return neighbors


def dfs_visual(app, x, y):
    if (x, y) in app.visited:
        return False

    app.visited.add((x, y))
    app.path.append((x, y))

    draw_maze(app.canvas, app.maze, app.visited, app.path)
    app.update_info()

    app.root.update()
    time.sleep(app.speed.get())

    if (x, y) == app.goal:
        return True

    for nx, ny in get_neighbors(app.maze, x, y):
        if dfs_visual(app, nx, ny):
            return True

    # backtracking
    app.path.pop()
    draw_maze(app.canvas, app.maze, app.visited, app.path)

    return False

    app.path.pop()
    draw_maze(app.canvas, app.maze, app.visited, app.path)

    return False



