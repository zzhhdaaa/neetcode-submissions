class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROW, COL = len(matrix), len(matrix[0])
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visit = set()
        memo = dict()
        res = 0
        
        def dfs(r: int, c: int, prev: int) -> int:
            if not 0<=r<ROW or not 0<=c<COL or matrix[r][c]<=prev:
                return 0
            
            if (r, c) in memo:
                return memo[(r, c)]
            
            total = 0
            # move in 4 dir
            for dr, dc in dirs:
                if (r+dr, c+dc) in visit:
                    continue
                visit.add((r+dr, c+dc))
                total = max(total, dfs(r+dr, c+dc, matrix[r][c]))
                visit.remove((r+dr, c+dc))
            memo[(r, c)] = 1 + total
            return memo[(r, c)]
        
        for r in range(ROW):
            for c in range(COL):
                visit.add((r, c))
                res = max(res, dfs(r, c, float('-inf')))
                visit.remove((r, c))
        
        return res
