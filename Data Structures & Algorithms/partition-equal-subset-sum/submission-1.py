class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        one = 0
        two = 0
        memo = dict()
        def dfs(i: int):
            nonlocal one
            nonlocal two

            if i >= len(nums):
                return one == two
            
            if (one, two, i) in memo:
                return memo[(one, two, i)]
            
            # put in one or two, then continue
            one += nums[i]
            putone = dfs(i+1)
            one -= nums[i]

            two += nums[i]
            puttwo = dfs(i+1)
            two -= nums[i]

            memo[(one, two, i)] = putone or puttwo
            return memo[(one, two, i)]
        
        return dfs(0)