class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac, atl = set(), set()
        ROWS, COLS = len(heights), len(heights[0])
        res = list()

        def dfs(row: int, col: int, visit: set, prevHeight: int):
            if ((row, col) in visit or
                row < 0 or col < 0 or row >= ROWS or col >= COLS or
                heights[row][col] < prevHeight): # notice here, we're going from the ocean to other side
                return
            visit.add((row, col))
            dfs(row+1, col, visit, heights[row][col])
            dfs(row-1, col, visit, heights[row][col])
            dfs(row, col+1, visit, heights[row][col])
            dfs(row, col-1, visit, heights[row][col])
        
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS-1, c, atl, heights[ROWS-1][c])
        
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS-1, atl, heights[r][COLS-1])
        
        for r,c in atl:
            if (r,c) in pac:
                res.append([r,c])
        
        return res