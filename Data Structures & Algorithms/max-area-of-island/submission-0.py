class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # loop through all the grid
        # if it is a land, dfs
        maxArea = 0
        curArea = 0

        def dfs(r: int, c: int):
            nonlocal grid
            nonlocal curArea

            if r not in range(len(grid)) or c not in range(len(grid[0])):
                return

            if grid[r][c] == 0:
                return

            grid[r][c] = 0
            curArea += 1

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    curArea = 0
                    dfs(r, c)
                    maxArea = max(maxArea, curArea)
        
        return maxArea