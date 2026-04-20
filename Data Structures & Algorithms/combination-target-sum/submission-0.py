class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # node
        # i, i+1
        # node node
        # i, i+1, i, i+l
        # i >= len(nums), or sum == target, or sum > target
        result = []
        curr = []
        # curr = [2, 2, 2, 2, ]

        def dfs(i: int):
            summary = sum(curr)
            if i >= len(nums) or summary > target:
                return
            elif summary == target:
                result.append(curr.copy())
                return
            
            # search with the current index
            curr.append(nums[i])
            dfs(i)

            # search with the next index
            curr.pop()
            dfs(i+1)
        
        dfs(0)
        return result
        


