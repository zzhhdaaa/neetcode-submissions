class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])

        # we do a dp along the r+c dir
        dp = [[0 for _ in range(COL)] for _ in range(ROW)]
        dp[0][0] = grid[0][0]

        # n = r + c
        for n in range(1, ROW+COL):
            for c in range(COL):
                r = n - c
                if not 0<=r<ROW or not 0<=c<COL:
                    continue
                top = dp[r-1][c] if r-1>=0 else float('inf')
                left = dp[r][c-1] if c-1>=0 else float('inf')
                dp[r][c] = grid[r][c] + min(top, left)

        return dp[ROW-1][COL-1]