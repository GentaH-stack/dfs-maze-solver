import tkinter as tk
import random

CELL_SIZE = 30


def generate_maze(rows, cols):
    """Generate a simple maze grid"""
    maze = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            maze[i][j] = random.choice([0, 1])
    maze[0][0] = 0
    maze[rows - 1][cols - 1] = 0
    return maze


def get_start_goal(maze):
    """Get start and goal positions"""
    return (0, 0), (len(maze) - 1, len(maze[0]) - 1)


def draw_maze(canvas, maze):
    """Draw the maze on canvas"""
    canvas.delete("all")
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            x1 = j * CELL_SIZE
            y1 = i * CELL_SIZE
            x2 = x1 + CELL_SIZE
            y2 = y1 + CELL_SIZE
            color = "#000000" if maze[i][j] == 1 else "#ffffff"
            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="#cccccc")


def dfs_visual(app, row, col):
    """Perform DFS with visualization"""
    if row < 0 or row >= len(app.maze) or col < 0 or col >= len(app.maze[0]):
        return False
    if (row, col) in app.visited or app.maze[row][col] == 1:
        return False

    app.visited.add((row, col))
    app.path.append((row, col))
    app.update_info()
    app.draw()
    app.root.update()

    if (row, col) == app.goal:
        return True

    app.root.after(int(app.speed.get() * 1000), lambda: None)

    for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        if dfs_visual(app, row + dr, col + dc):
            return True

    app.path.pop()
    return False


class MazeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("DFS Maze Solver")

        self.maze = generate_maze(10, 10)
        self.start, self.goal = get_start_goal(self.maze)

        self.visited = set()
        self.path = []

        self.canvas = tk.Canvas(root, bg="#ffffff")
        self.canvas.pack(pady=10)

        frame = tk.Frame(root)
        frame.pack()

        tk.Button(frame, text="▶ Start DFS", command=self.start_dfs, bg="#06d6a0", fg="white").grid(row=0, column=0,
                                                                                                    padx=5)
        tk.Button(frame, text="🔄 Reset", command=self.reset, bg="#118ab2", fg="white").grid(row=0, column=1, padx=5)
        tk.Button(frame, text="🎲 Random Maze", command=self.random_maze, bg="#8338ec", fg="white").grid(row=0, column=2,
                                                                                                        padx=5)

        self.speed = tk.DoubleVar(value=0.1)
        tk.Scale(root, from_=0.01, to=0.5, resolution=0.01,
                 orient="horizontal", label="Speed", variable=self.speed).pack()

        self.status = tk.StringVar(value="Ready")
        self.info = tk.StringVar(value="Visited Nodes: 0")

        tk.Label(root, textvariable=self.status, fg="#333").pack()
        tk.Label(root, textvariable=self.info, fg="#555").pack()

        self.draw()

    def draw(self):
        rows = len(self.maze)
        cols = len(self.maze[0])

        self.canvas.config(width=cols * CELL_SIZE, height=rows * CELL_SIZE)
        draw_maze(self.canvas, self.maze)

    def update_info(self):
        self.info.set(f"Visited Nodes: {len(self.visited)}")

    def start_dfs(self):
        self.visited = set()
        self.path = []

        self.status.set("Searching...")

        found = dfs_visual(self, self.start[0], self.start[1])

        if found:
            self.status.set("✅ Path Found!")
        else:
            self.status.set("❌ No Path Found!")

    def reset(self):
        self.visited = set()
        self.path = []
        self.status.set("Reset done")
        self.draw()

    def random_maze(self):
        self.maze = generate_maze(10, 10)
        self.start, self.goal = get_start_goal(self.maze)
        self.reset()


if __name__ == "__main__":
    root = tk.Tk()
    app = MazeApp(root)
    root.mainloop()