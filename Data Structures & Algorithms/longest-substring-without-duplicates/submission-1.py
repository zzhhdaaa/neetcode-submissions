class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        left = 0
        length = 1
        hashset = set()
        hashset.add(s[left])

        for right in range(1, len(s)):
            while s[right] in hashset:
                hashset.remove(s[left])
                left += 1
            hashset.add(s[right])
            if right-left+1 > length:
                length = right-left+1
        
        return length
        