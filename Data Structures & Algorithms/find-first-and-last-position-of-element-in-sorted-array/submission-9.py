import bisect

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = bisect.bisect_left(nums, target)
        print(start)
        start = start if 0<=start<len(nums) and nums[start] == target else -1

        end = bisect.bisect_right(nums, target) - 1
        end = end if 0<=end<len(nums) and nums[end] == target else -1

        return [start, end]