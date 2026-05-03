class Solution:
    def rob(self, nums: List[int]) -> int:
        # 1 2 3 2
        # _ (0,True): 1, (0,False):0     (idx, rob this): max rob
        if len(nums) == 1:
            return nums[0]

        memo0 = dict() # does not rob the first one
        memo1 = dict() # rob the first one

        memo0[(0,False)] = 0
        memo1[(0,True)] = nums[0]

        for i in range(1, len(nums)):
            memo0[(i,True)] = memo0.get((i-1,False), 0) + nums[i]
            memo0[(i,False)] = max(memo0.get((i-1,True), 0), memo0.get((i-2,True), 0))
            memo1[(i,True)] = memo1.get((i-1,False), 0) + nums[i]
            memo1[(i,False)] = max(memo1.get((i-1,True), 0), memo1.get((i-2,True), 0))
        
        roblastmax = memo0.get((len(nums)-1,True), 0)
        robfirstmax = memo1.get((len(nums)-1,False), 0)

        return max(robfirstmax, roblastmax)