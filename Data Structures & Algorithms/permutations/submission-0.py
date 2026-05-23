class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visit = set()
        curr = []
        res = []

        def dfs(num: int):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            
            for i in range(len(nums)):
                if nums[i] in visit:
                    continue
                visit.add(nums[i])
                curr.append(nums[i])
                dfs(nums[i])
                curr.pop()
                visit.remove(nums[i])
        
        for num in nums:
            visit.add(num)
            curr.append(num)
            dfs(num)
            curr.pop()
            visit.remove(num)
        
        return res