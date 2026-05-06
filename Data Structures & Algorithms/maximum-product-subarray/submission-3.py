class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # since there's negative numbers, we need to track min and max
        res = float('-inf')
        minP = 1
        maxP = 1
        maxN = float('-inf')

        for num in nums:
            maxN = max(maxN, num)

            if num == 0:
                minP = 1
                maxP = 1
                res = max(res, 0)
                continue
            
            temp = minP
            minP = min(temp*num, maxP*num, num)
            maxP = max(temp*num, maxP*num, num)

            res = max(res, maxP)

            minP = min(minP, 1)
            maxP = max(maxP, 1)
        return res