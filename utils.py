CELL_SIZE = 40

def draw_maze(canvas, maze, visited=set(), path=[]):
    canvas.delete("all")

    for i in range(len(maze)):
        for j in range(len(maze[0])):
            x1 = j * CELL_SIZE
            y1 = i * CELL_SIZE
            x2 = x1 + CELL_SIZE
            y2 = y1 + CELL_SIZE

            cell = maze[i][j]

            if cell == 1:
                color = "#1e1e1e"  # mur
            elif (i, j) in path:
                color = "#ffd166"  # rruga finale
            elif (i, j) in visited:
                color = "#4cc9f0"  # e vizituar
            else:
                color = "#f8f9fa"  # bosh

            if cell == 'S':
                color = "#06d6a0"
            elif cell == 'G':
                color = "#ef476f"

            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="#adb5bd")

    canvas.update()   