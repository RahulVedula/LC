class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n, m = len(matrix), len(matrix[0])
        self.matrix = matrix
        self.column_sum = [[0 for _ in range(m)] for _ in range(n)]
        self.corner_sum = [[0 for _ in range(m)] for _ in range(n)]


        for j in range(m):
            for i in range(n):
                self.column_sum[i][j] = matrix[i][j] + self.column_sum[i-1][j] if i != 0 else matrix[i][j]
        
        for i in range(n):
             for j in range(m):
                if j == 0:
                    self.corner_sum[i][j] = self.column_sum[i][j]
                else:
                    self.corner_sum[i][j] = self.corner_sum[i][j-1] + self.column_sum[i][j]
        
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 == 0 and col1 == 0:
            return self.corner_sum[row2][col2]

        elif row1 == 0:
            return self.corner_sum[row2][col2] - self.corner_sum[row2][col1-1]
        
        elif col1 == 0:
            return self.corner_sum[row2][col2] - self.corner_sum[row1-1][col2]


        upper = self.corner_sum[row1-1][col2]
        left = self.corner_sum[row2][col1-1]
        bottom = self.corner_sum[row1-1][col1-1]
        total = self.corner_sum[row2][col2]
        return total-upper-left+bottom
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)