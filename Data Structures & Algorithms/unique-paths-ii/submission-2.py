class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        
        # x x x x
        # x x x
        # x x
        ROW, COL = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(COL)] for _ in range(ROW)]
        dp[0][0] = 1

        # n = r + c
        for n in range(1, ROW+COL):
            for c in range(max(0, n-ROW), COL):
                r = n-c
                if not 0<=r<ROW or not 0<=c<COL or obstacleGrid[r][c] == 1:
                    continue
                top = dp[r-1][c] if r-1>=0 else 0
                left = dp[r][c-1] if c-1>=0 else 0
                dp[r][c] = top + left
        
        return dp[ROW-1][COL-1]