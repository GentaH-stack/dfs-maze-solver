class MazeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("DFS Maze Solver")

        self.maze = create_maze()
        self.start, self.goal = get_start_goal(self.maze)

        self.visited = set()
        self.path = []

        # Canvas
        self.canvas = tk.Canvas(root, bg="#ffffff")
        self.canvas.pack(pady=10)

        # Buttons
        frame = tk.Frame(root)
        frame.pack()

        tk.Button(frame, text="▶ Start DFS", command=self.start_dfs, bg="#06d6a0", fg="white").grid(row=0, column=0, padx=5)
        tk.Button(frame, text="🔄 Reset", command=self.reset, bg="#118ab2", fg="white").grid(row=0, column=1, padx=5)
        tk.Button(frame, text="🎲 Random Maze", command=self.random_maze, bg="#8338ec", fg="white").grid(row=0, column=2, padx=5)