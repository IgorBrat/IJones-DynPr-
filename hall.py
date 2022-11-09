class Hall:
    def __init__(self, filein: str):
        print(f"\n\nStarted application for {filein}")
        print("="*30)
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
        self.dp = [[0 for i in range(self.width)] for j in range(self.height)]

    def __bottom_up(self, row, col):
        if self.dp[row][col]:
            res = self.dp[row][col]
        else:
            res = 0
            if col != self.width - 1:
                for i in range(self.height - 1, -1, -1):
                    for j in range(self.width - 1, col, -1):
                        if self.hall[i][j] == self.hall[row][col] or (i == row and j == col + 1):
                            res += self.dp[i][j]
        return res

    def __get_paths(self, out_row, out_col):
        self.dp[out_row][out_col] = 1
        res = [0 for j in range(self.height)]
        for col in range(self.width - 1, -1, -1):
            for row in range(self.height - 1, -1, -1):
                self.dp[row][col] = self.__bottom_up(row, col)
        for i in range(self.height):
            res[i] += self.dp[i][0]
        return sum(res)

    def find_all_paths(self):
        if self.height != 1:
            res = self.__get_paths(self.height - 1, self.width - 1)
            self.dp = [[0 for i in range(self.width)] for j in range(self.height)]
            res += self.__get_paths(0, self.width - 1)
        else:
            res = self.__get_paths(0, self.width - 1)
        self.__write_res_combinations(res)
        print("Finished calculating")

    def __write_res_combinations(self, all_unique_paths: int):
        with open(self.fileout, 'w') as fileout:
            fileout.write("All unique paths: " + str(all_unique_paths))
