class Solution:
    def rob(self, nums: List[int]) -> int:
        # 1 2 3 4 1
        # _ [0,True]: 1, [0,False]: 0
        #   _ [1,True]: 2+[0,False], [1,False]: [0,True]

        memo = dict()
        
        for i in range(len(nums)):
            memo[(i,True)] = memo.get((i-1,False), 0) + nums[i]
            memo[(i,False)] = max(memo.get((i-1,True), 0), memo.get((i-1,False), 0))
        
        return max(memo[(len(nums)-1,True)], memo[(len(nums)-1,False)])
