class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # wordSet = set(wordDict)
        # memo = dict()
        
        # def dfs(i: int, curr: str) -> bool:
        #     if (i, curr) in memo:
        #         return memo[(i, curr)]
            
        #     if i == len(s):
        #         return curr in wordSet
            
        #     if curr in wordSet:
        #         memo[(i, curr)] = dfs(i+1, s[i]) or dfs(i+1, curr+s[i])
        #     else:
        #         memo[(i, curr)] = dfs(i+1, curr+s[i])
            
        #     return memo[(i, curr)]
        
        # return dfs(0, "")

        # The above is working but slow, could take O N^2
        # The question your dfs function should answer is: 
        # "Can the substring from index start to the end of the string 
        # be broken down into dictionary words?"

        # True dp bottom up solution
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True # the end

        for i in range(len(s)-1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i:i+len(w)] == w:
                    dp[i] = dp[i+len(w)]
                if dp[i]:
                    break
        
        return dp[0]
