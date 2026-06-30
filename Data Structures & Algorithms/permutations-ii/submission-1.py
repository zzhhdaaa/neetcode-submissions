class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = set()

        def backtrack(perm):
            if len(perm) == len(nums):
                res.add(tuple(perm))
                return
            
            for i in range(len(nums)):
                if nums[i] == float('inf'):
                    continue
                perm.append(nums[i])
                nums[i] = float('inf')
                backtrack(perm)
                nums[i] = perm.pop()
        
        backtrack([])
        return list(res)