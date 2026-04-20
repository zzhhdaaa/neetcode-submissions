class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []

        def dfs(i: int):
            if i >= len(nums):
                result.append(subset.copy())
                return
            
            # continue search on the "take" branch
            subset.append(nums[i])
            dfs(i+1)

            # continue search on the "none" branch
            subset.pop()
            dfs(i+1)
        
        dfs(0)
        return result

