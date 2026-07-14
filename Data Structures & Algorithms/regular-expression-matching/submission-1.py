class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = dict()
        
        def dfs(i: int, j: int) -> bool:
            if (i, j) in memo:
                return memo[(i, j)]
            
            if i < 0 and j < 0:
                return True
            elif j < 0:
                # the p is used up
                return False
            
            res = False
            if i >= 0 and (p[j] == '.' or s[i] == p[j]):
                res =  dfs(i-1, j-1)
            elif p[j] == '*':
                # end the * counting period
                res = dfs(i, j-2)
                if i >= 0 and (s[i] == p[j-1] or p[j-1] == '.'):
                    # take account one previous, don't move j, or move j
                    res = res or dfs(i-1, j) or dfs(i-1, j-2)
            
            memo[(i, j)] = res
            return res
        
        return dfs(len(s)-1, len(p)-1)