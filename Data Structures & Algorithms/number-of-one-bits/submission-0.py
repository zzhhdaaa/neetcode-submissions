class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        i = 0

        while i < 32:
            res += n & 1 == 1
            n = n >> 1
            i += 1
        
        return res