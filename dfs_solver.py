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
