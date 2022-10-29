from ijones.node import Node


class Hall:
    def __init__(self, filein: str):
        with open(filein) as file:
            hall = file.read().splitlines()
        dimensions = hall[0].split(" ")
        self.width, self.height  = int(dimensions[0]), int(dimensions[1])
        self.hall = []
        for i in range(1, self.height + 1):
            row = []
            for j in range(self.width):
                row.append(hall[i][j])
            self.hall.append(row)
        print("Hall: " + str(self.hall))
        if self.height > 1:
            self.out = [(0, self.width - 1), (self.height - 1, self.width - 1)]
        else:
            self.out = [(self.height - 1, self.width - 1)]
        print("Out: " + str(self.out))
        print("="*60)

    def get_candidates(self, position: tuple):
        row, column = position
        candidates = []
        for i in range(self.height):
            for j in range(column + 1, self.width):
                if (i == row and j == column + 1) or (self.hall[row][column] == self.hall[i][j]):
                    candidates.append((i, j))
        return candidates

    def __get_path(self, node: Node):
        path = [node]
        while node.parent is not None:
            node = node.parent
            path.append(node)
        return list(reversed(path))

    def dfs_modified(self, start: tuple):
        if start[0] not in range(self.height) or start[1] not in range(self.width):
            raise IndexError("Element is out of bonds of the maze")
        stack = []
        start = Node(self.hall[start[0]][start[1]], start)
        stack.append(start)
        while len(stack) != 0:
            node = stack.pop(0)
            if node.position in self.out:
                print("Path: " + str(self.__get_path(node)))
            for position in self.get_candidates(node.position):
                stack.append(Node(self.hall[position[0]][position[1]], position, node))
