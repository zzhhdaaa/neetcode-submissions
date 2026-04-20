class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        lengths = dict()

        for num in nums_set:
            if num-1 not in nums_set:
                lengths[num] = 1
        
        max_length = 0
        for starter in lengths.keys():
            while starter+lengths[starter] in nums_set:
                lengths[starter] += 1

            if lengths[starter] > max_length:
                max_length = lengths[starter]
        
        return max_length