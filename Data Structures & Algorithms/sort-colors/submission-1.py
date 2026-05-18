class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums)-1 # pointing to the future 0 location and 2 location
        i = 0

        def swap(x, y):
            tmp = nums[x]
            nums[x] = nums[y]
            nums[y] = tmp

        while i<=r:
            if nums[i] == 0:
                swap(i, l)
                l += 1
                i += 1 # we increment i because the left side is gauranteed to be sorted
            elif nums[i] == 1:
                # do nothing
                i += 1
            elif nums[i] == 2:
                swap(i, r)
                r -= 1
                # we don't increment i here because the right side could still has more position to place a 2
        
