class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # we turn the problem into finding the max and min subarray sum
        # so that the res = max(max subarray, sum - min subarray)

        curr = 0
        prefix = [] # all numbers added up till i
        maxsub = float('-inf')
        minsub = float('inf')
        maxprefix = float('-inf')
        minprefix = 0
        for num in nums:
            curr += num
            prefix.append(curr)
            maxsub = max(maxsub, curr-minprefix)
            minsub = min(minsub, curr-maxprefix)
            maxprefix = max(maxprefix, curr)
            minprefix = min(minprefix, curr)
        
        return max(maxsub, prefix[-1]-minsub)
