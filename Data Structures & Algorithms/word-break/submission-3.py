class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        memo = dict()
        
        def dfs(i: int, curr: str) -> bool:
            if (i, curr) in memo:
                return memo[(i, curr)]
            
            if i == len(s):
                return curr in wordSet
            
            if curr in wordSet:
                memo[(i, curr)] = dfs(i+1, s[i]) or dfs(i+1, curr+s[i])
            else:
                memo[(i, curr)] = dfs(i+1, curr+s[i])
            
            return memo[(i, curr)]
        
        return dfs(0, "")