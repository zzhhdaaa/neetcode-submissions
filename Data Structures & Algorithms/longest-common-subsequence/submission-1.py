class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # dp[i][j] = longest common sub in text1[:i+1] and text2[:j+1]
        dp = [[0 for _ in range(len(text2))] for _ in range(len(text1))]

        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    # use the current chars as a match
                    # so we should look at the dp without both current chars
                    diag = dp[i-1][j-1] if i>0 and j>0 else 0
                    dp[i][j] = diag + 1
                else:
                    # the current could not be a match
                    # so we should look at dp without each of current chars 
                    up = dp[i-1][j] if i-1>=0 else 0
                    left = dp[i][j-1] if j-1>=0 else 0
                    dp[i][j] = max(up, left)
        
        return dp[-1][-1]