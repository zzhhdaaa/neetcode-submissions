class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(i: int, prev: list):
            if i >= len(nums):
                res.append(prev.copy())
                return
            
            prev.append(nums[i])
            dfs(i+1, prev)
            num = prev.pop()
            pt = i+1
            while pt < len(nums) and nums[pt] == num:
                pt += 1
            dfs(pt, prev)

        dfs(0, [])
        return res