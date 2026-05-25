class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l = 0
        r = len(nums) - 1

        while l<=r:
            m = (l+r) // 2

            left = nums[l]
            mid = nums[m]
            right = nums[r]

            print(l, m, r)

            if left == target or mid == target or right == target:
                return True

            # if left > mid:
            #     # turning point in left
            # elif mid > right:
            #     # turning point in right
            # else:
            #     # all sorted, or unidentifiable
            
            if left <= target <= mid:
                # left is sorted, and target in left
                print(1)
                r = m - 1
                continue
            elif mid <= target <= right:
                # right is sorted, and target in right
                print(2)
                l = m + 1
                continue
            elif left > mid and (target > left or target < mid):
                print(3)
                r = m - 1
                continue
            elif mid > right and (target > mid or target < right):
                print(4)
                l = m + 1
                continue
            else:
                # unable to identify which part it's in, so shift the left till not duplicating
                l = l + 1
                while l < len(nums) and nums[l-1] == nums[l]:
                    l = l + 1
        
        return False
