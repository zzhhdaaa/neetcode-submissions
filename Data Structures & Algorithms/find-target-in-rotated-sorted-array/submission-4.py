class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # first, find the rotated times
        # 3, 4, 5, 6, 1, 2
        # _     _        _
        #       _        _
        # 3, 4, 5, 6, 1, 2, (3), (4), (5), (6)
        #            [4]                   [9]

        l = 0
        r = len(nums) - 1

        while l < r:
            if nums[l] <= nums[r]:
                break
            m = (l+r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1
        
        # at this point, l is already the sorted start of the list
        rotated = l
        # print(l)
        r = l + len(nums) - 1

        while l <= r:
            m = (l+r) // 2
            trueL = l % len(nums)
            trueR = r % len(nums)
            trueM = m % len(nums)

            # if target > nums[trueR] or target < nums[trueL]:
            #     print(l)
            #     print(trueL)
            #     print(nums[trueL])
            #     return -1

            if nums[trueL] == target:
                return trueL
            elif nums[trueR] == target:
                return trueR
            elif nums[trueM] == target:
                return trueM
            
            if nums[trueM] < target:
                l = m + 1
            elif nums[trueM] > target:
                r = m - 1
            
        return -1

