class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        heapq.heapify(nums)
        
        res = 1
        curr = heapq.heappop(nums)

        while curr <= 0 and len(nums) > 0:
            curr = heapq.heappop(nums)

        while curr == res:
            res += 1
            prev = curr
            if len(nums) > 0:
                curr = heapq.heappop(nums)
            while len(nums) > 0 and curr == prev:
                curr = heapq.heappop(nums)
        
        return res