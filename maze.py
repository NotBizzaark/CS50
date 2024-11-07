import sys

class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action

class StackFrontier():
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)
    
    def empty(self):
        return len(self.frontier) == 0
    
    def remove(self):
        if self.empty():
            raise Exception("Frontier Empty!!!!")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node
        
class QueueFrontier(StackFrontier):
    def remove(self):
        if self.empty():
            raise Exception("Frontier Empty!!!!")
        else:
            node = self.frontier[1]
            self.frontier = self.frontier[1:]
            return node
        
class Maze():
    def __init__(self, filename):
        with open(filename) as f:
            contents = f.read()

        if contents.count("A") != 1:
            raise Exception("Must have exactly one 'A' statring point")
        if contents.count("B") !=1:
            raise Exception("Must have exactly one 'B' ending point")
        
        contents = contents.splitlines()
        self.height = len(contents)
        self.width = max(len(line) for line in contents)

        self.wall = []

        for i in range(self.height):
            rows = []
            for j in range(self.width):
                try:
                    if contents[i][j] == "A":
                        self.start = (i,j)
                        rows.append(False)
                    elif contents[i][j] == "B":
                        self.end = (i,j)
                        rows.append(False)
                    elif contents[i][j] == " ":
                        rows.append(False)
                    else:
                        rows.append(True)
                except IndexError:
                    rows.append(False)
            self.walls.append(rows)

            self.solution = None

    def print(self):
        solution = self.solution[1] if self.solution is not None else None
        print()
        for i, row in enumerate(self.walls):
            for j, col in enumerate(row):
                if col:
                    print("|", end="")
                elif (i,j) == self.start:
                    print("A", end="")
                elif (i,j) == self.end:
                    print("B", end="")
                elif solution is not None and (i, j) in solution:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
        print()

    def neighbor(self, state):
        row, col = state
        if state == "end":
            print("end")
        else:
            pass
