class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # brute force
        res = []
        def dfs(i: int, prev: List[int]):
            if i >= len(nums):
                res.append(prev.copy())
                return
            
            prev.append(nums[i])
            dfs(i+1, prev)
            prev.pop()
            dfs(i+1, prev)

        dfs(0, [])
        return list(res)