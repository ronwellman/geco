#!/usr/bin/env python3
import time
import os
import sys
from maze_support import Maze


class Solver:
    """
    class Solver attempts to solve a maze. It does not perform any
    optimizations (shortest path) but instead performs a quasi depth first
    search until it finds the endpoint.
    """

    def __init__(self, maze):
        # store the maze
        self.maze = maze

        # get the start position


        # End is not known
        self.end = None

        # current position is the start position


        # create a visited and seen set (sets will only contain unique entries)
        # visited (solver has been here)
        # seen (solver has been near here)



        # create a path record of where we have been (list)


        # record that we have visited and seen the start


        # initially look at what surrounds current position
   

    @staticmethod
    def left(position):
        """
        left(tuple) -> tuple

        Returns position moved left by 1.
        """
        row, col = position
        return (row, col - 1)

    @staticmethod
    def right(position):
        """
        right(tuple) -> tuple

        Returns position moved right by 1.
        """
        row, col = position
        return (row, col + 1)

    @staticmethod
    def up(position):
        """
        up(tuple) -> tuple

        Returns position moved up by 1.
        """
        row, col = position
        return (row - 1, col)

    @staticmethod
    def down(position):
        """
        down(tuple) -> tuple

        Returns position moved down by 1.
        """
        row, col = position
        return (row + 1, col)

    def _query_quadrants(self):
        """
        _query_quadrants() -> NoneType

        Peers into the four coordinates around the current position.
        """

        # update seen up, down, left, and right





    def _update_seen(self, position):
        """
        _update_seen(tuple) -> NoneType

        Checks the position and updates seen if position is empty.
        """

        # query the maze for what is at row, col
        value = self.maze.get_point(position)

        # Only update seen if position is blank or End point
        if value == " " or value == "E":
            self.seen.add(position)

        # if position is End Point, record it in self.end
        if value == "E":
            self.end = position

    def search(self):
        """
        search() -> NoneType

        Continues to move around until all all nodes have been visited.
        """
        while True:

            # determine if we have visited all known positions
            unvisited = self.seen.difference(self.visited)
            
            if len(unvisited) == 0:
                break

            # choose a direction to go
            if self.end is not None:

            elif 

            elif

            elif

            elif

            else:
                # last entry in path is where solver is currently standing
                self.path.pop()

                # move to previous position


            # take a look at surrounding positions
            self._query_quadrants()

            # take a quick sleep so we can watch the progress of the search
            time.sleep(0.1)

            # clear the screen
            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")

            # print solver's progress
            print(self)

            # check to see if we've reached the end
            if self.end is not None:
                break

    def _update_pos(self, position):
        """
        update_pos(tuple) -> NoneType

        Updates current position.
        """
        # update current position
        self.curr_pos = position

        # add new position to path (list)
        self.path.append(self.curr_pos)

        # add new position to visited (set)
        self.visited.add(self.curr_pos)

    def __str__(self):
        """
        __str__() -> str

        Print the current state of the maze.
        """
        # if maze has been solved, only show path that was taken
        if self.end is not None:
            return self.maze.__str__(self.path, self.curr_pos)

        return self.maze.__str__(self.visited, self.curr_pos)


if __name__ == "__main__":

    # check to see if a path to the maze was passed to the program
    if len(sys.argv) != 2:
        print("Invalid usage:")
        print("\nmaze_solver.py MAZE")
        sys.exit(0)

    # create a maze object
    maze = Maze(sys.argv[1])
    if maze is None:
        print("Unable to load maze: {}".format(sys.argv[1]))
        sys.exit(0)

    # create a solver object


    # instruct solver to search for the endpoint


    # check to see if solver was able to solve the maze
    if solver.end is None:
        print("Unable to solve...")
    else:
        print("Solved!!!")
