import os


class Maze:
    """
    Maze loads and allows the querying of the maze.
    """

    def __new__(cls, maze_path):
        if not os.path.exists(maze_path):
            return None
        instance = super().__new__(cls)
        instance.maze = instance._load_maze(maze_path)
        return instance

    @classmethod
    def _load_maze(cls, maze_path):
        """
        load_maze(PATH) -> list of lists

        Loads in an ASCII file for the maze and returns a list of lists for the
        maze.
        """
        new_maze = []

        # read line by line
        with open(maze_path, "r") as maze:
            for row in maze.readlines():
                new_maze.append([col for col in row.rstrip("\n")])

        return new_maze

    def get_point(self, point):
        """
        get_point(tuple) -> str

        Returns the character at the row and column or None if not found.
        """
        row, col = point
        
        try:
            return self.maze[row][col]
        except IndexError:
            return None

    def get_start(self):
        """
        get_start() -> tuple

        Returns a tuple of the row and column numbers that identifies where 'S'
        is in the maze.
        """
        for row, row_list in enumerate(self.maze):
            for col, val in enumerate(row_list):
                if val == "S":
                    return (row, col)

        return None

    def __str__(self, visited=None, curr_pos=None):
        """
        __str__(set=None, tuple=None) -> str

        Given a set of coordinates and current position, print the current
        state of the maze.  Otherwise, just print the maze.
        """
        maze = []

        if visited is None or curr_pos is None:
            return "\n".join(("".join(row) for row in self.maze))
        else:
            for r, row in enumerate(self.maze):
                for c, spot in enumerate(row):
                    if (r, c) == curr_pos:
                        maze.append("O")
                    elif (r, c) in visited:
                        maze.append("~")
                    else:
                        maze.append(spot)
                maze.append("\n")
            return "".join(maze)
