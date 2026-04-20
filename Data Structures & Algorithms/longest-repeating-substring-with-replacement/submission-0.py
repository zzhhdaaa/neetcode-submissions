class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def minReplacement(s: str) -> int:
            count = dict()
            for c in s:
                count[c] = 1 if c not in count.keys() else count[c]+1
            return sum(count.values()) - max(count.values())
        
        if len(s) == 1:
            return 1

        maxLen = 1
        left = 0
        for right in range(1, len(s)):
            while minReplacement(s[left:right+1]) > k:
                left += 1
            maxLen = max(maxLen, right+1-left)
        
        return maxLen
            
            