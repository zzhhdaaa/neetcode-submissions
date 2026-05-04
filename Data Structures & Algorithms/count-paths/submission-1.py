class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = dict()
        def dfs(row, col) -> int:
            if not (0<=row<m and 0<=col<n):
                # out of bound
                return 0
            
            if row == m-1 and col == n-1:
                # found path
                return 1
            
            if (row,col) in memo:
                return memo[(row,col)]
            
            right = dfs(row, col+1)
            down = dfs(row+1, col)
            memo[(row,col)] = right+down

            return right+down
        
        return dfs(0, 0)