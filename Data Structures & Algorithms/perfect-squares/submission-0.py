class Solution:
    def numSquares(self, n: int) -> int:
        top = int(n**0.5)
        nums = [x for x in range(top, 0, -1)]
        memo = dict()

        def dfs(i: int, remain: int) -> int:
            if remain == 0:
                return 0
            
            if (i, remain) in memo:
                return memo[(i, remain)]
            
            if i >= len(nums):
                return float('inf')
            
            res = float('inf')
            sqr = nums[i]*nums[i]
            # take this vs skip this
            if sqr <= remain:
                res = min(res, dfs(i, remain-sqr)+1)
            res = min(res, dfs(i+1, remain))
            memo[(i, remain)] = res
            return res
        
        return dfs(0, n)