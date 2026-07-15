class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])

        def getCell(r: int, c: int) -> int:
            if r < 0 or r >= ROW or c < 0 or c >= COL:
                return 0
            return grid[r][c]
        
        res = 0

        for r in range(ROW):
            prev = 0
            for c in range(-1, COL+1):
                curr = getCell(r, c)
                if prev != curr:
                    res += 1
                    prev = curr

        for c in range(COL):
            prev = 0
            for r in range(-1, ROW+1):
                curr = getCell(r, c)
                if prev != curr:
                    res += 1
                    prev = curr
        
        return res