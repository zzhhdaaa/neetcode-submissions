class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        prefix = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                top = prefix[i-1][j] if i-1>=0 else 0
                left = prefix[i][j-1] if j-1>=0 else 0
                overlap = prefix[i-1][j-1] if i-1>=0 and j-1>=0 else 0
                prefix[i][j] = top + left - overlap + matrix[i][j]
        self.prefix = prefix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # if we want to calculate (r1, c1) to (r2, c2)
        top = self.prefix[row1-1][col2] if row1-1>=0 else 0
        left = self.prefix[row2][col1-1] if col1-1>=0 else 0
        overlap = self.prefix[row1-1][col1-1] if row1-1>=0 and col1-1>=0 else 0
        return self.prefix[row2][col2] - top - left + overlap


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)