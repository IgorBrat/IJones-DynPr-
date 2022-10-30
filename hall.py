from ijones.node import Node


class Hall:
    def __init__(self, filein: str):
        self.fileout = filein.split(".")[0] + ".out"
        with open(filein) as file:
            hall = file.read().splitlines()
        dimensions = hall[0].split(" ")
        self.width, self.height = int(dimensions[0]), int(dimensions[1])
        self.hall = []
        for i in range(1, self.height + 1):
            row = []
            for j in range(self.width):
                row.append(hall[i][j])
            self.hall.append(row)
        if self.height > 1:
            self.out = [(0, self.width - 1), (self.height - 1, self.width - 1)]
        else:
            self.out = [(self.height - 1, self.width - 1)]
        self.explored_paths = {}

    def __get_candidates(self, position: tuple):
        row, column = position
        candidates = []
        for i in range(self.height):
            for j in range(column + 1, self.width):
                if (i == row and j == column + 1) or (self.hall[row][column] == self.hall[i][j]):
                    candidates.append((i, j))
        return candidates

    @staticmethod
    def __get_path(node: Node):
        path = [node]
        while node.parent is not None:
            node = node.parent
            path.append(node)
        return path

    def __dfs_modified(self, start: tuple):
        if start[0] not in range(self.height) or start[1] not in range(self.width):
            raise IndexError("Element is out of bonds of the maze")
        stack = []
        start = Node(self.hall[start[0]][start[1]], start)
        stack.append(start)
        while len(stack) != 0:
            node = stack.pop()
            if node.position in self.explored_paths.keys():
                curr_pos_paths_count = self.explored_paths[node.position]
                curr_path = self.__get_path(node)
                for parent_node in curr_path:
                    if parent_node.position != node.position:
                        if parent_node.position in self.explored_paths.keys():
                            self.explored_paths[parent_node.position] += curr_pos_paths_count
                        else:
                            self.explored_paths[parent_node.position] = curr_pos_paths_count
            elif node.position in self.out:
                curr_path = self.__get_path(node)
                for curr_node in curr_path[1:]:
                    if curr_node.position not in self.explored_paths.keys():
                        self.explored_paths[curr_node.position] = 1
                    else:
                        self.explored_paths[curr_node.position] += 1
            else:
                for position in self.__get_candidates(node.position):
                    candidate_node = Node(self.hall[position[0]][position[1]], position, node)
                    stack.append(candidate_node)
        return self.explored_paths[(start.position[0], start.position[1])]

    def get_all_unique_paths(self):
        print("Started application")
        print("=" * 60)
        print("Processing...\n")
        all_unique_paths = 0
        for row in range(self.height):
            all_unique_paths += self.__dfs_modified((row, 0))
        self.__write_res_combinations(all_unique_paths)
        print(f"Successfully written result to {self.fileout}\n\n\n")

    def __write_res_combinations(self, all_unique_paths: int):
        with open(self.fileout, 'w') as fileout:
            fileout.write("All unique paths: " + str(all_unique_paths))
