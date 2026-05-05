class Solution:
    def numDecodings(self, s: str) -> int:
        # 1 0 1 2
        # what decision tree?
        # at current idx, pick single or pick double

        memo = dict()

        def dfs(i: int, last: str):
            # block when unsuccessful
            if len(last) != 0 and (last[0] == "0" or not 1<=int(last)<=26):
                return 0 
            
            # return 1 when reach end
            if i >= len(s):
                return 1
            
            # return memo
            if i in memo:
                return memo[i]
            
            single = dfs(i+1, s[i])
            double = dfs(i+2, s[i]+s[i+1]) if i+1 < len(s) else 0
            memo[i] = single + double
            return memo[i]
        
        dfs(0, "")
        return memo[0]
