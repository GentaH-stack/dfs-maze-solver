import tkinter as tk
from maze import generate_maze, get_start_goal
from dfs_solver import dfs_visual
from utils import draw_maze, CELL_SIZE


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

        tk.Button(frame, text="▶ Start DFS", command=self.start_dfs, bg="#06d6a0", fg="white").grid(row=0, column=0, padx=5)
        tk.Button(frame, text="🔄 Reset", command=self.reset, bg="#118ab2", fg="white").grid(row=0, column=1, padx=5)
        tk.Button(frame, text="🎲 Random Maze", command=self.random_maze, bg="#8338ec", fg="white").grid(row=0, column=2, padx=5)

        self.speed = tk.DoubleVar(value=0.1)
        tk.Scale(root, from_=0.01, to=0.5, resolution=0.01,
                 orient="horizontal", label="Speed", variable=self.speed).pack()

        self.status = tk.StringVar(value="Ready")
        self.info = tk.StringVar(value="Visited Nodes: 0")

        tk.Label(root, textvariable=self.status).pack()
        tk.Label(root, textvariable=self.info).pack()

        self.draw()

    def draw(self):
        rows = len(self.maze)
        cols = len(self.maze[0])

        self.canvas.config(width=cols * CELL_SIZE, height=rows * CELL_SIZE)
        draw_maze(self.canvas, self.maze, self.visited, self.path)

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