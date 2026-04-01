def draw_maze(canvas, maze, visited=set(), path=[]):
    canvas.delete("all")

    for i in range(len(maze)):
        for j in range(len(maze[0])):
            x1 = j * CELL_SIZE
            y1 = i * CELL_SIZE
            x2 = x1 + CELL_SIZE
            y2 = y1 + CELL_SIZE

            cell = maze[i][j]