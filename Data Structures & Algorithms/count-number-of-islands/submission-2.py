class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        islands = 0

        def dfs(row: int, col: int):
            # out of bound
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
                return

            # already "water"
            if grid[row][col] == "0":
                return
            
            # mark as "water"
            grid[row][col] = "0"
            dfs(row-1, col)
            dfs(row+1, col)
            dfs(row, col-1)
            dfs(row, col+1)
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    dfs(row, col)
                    islands += 1
        
        return islands
