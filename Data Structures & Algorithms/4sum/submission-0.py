class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        count = defaultdict(int)

        for num in nums:
            count[num] += 1

        res = []
        # brute force
        for i in range(len(nums)):
            if 0<=i-1<len(nums) and nums[i-1]==nums[i]:
                continue
            count[nums[i]] -= 1

            for j in range(i+1, len(nums)):
                if i+1<=j-1<len(nums) and nums[j-1]==nums[j]:
                    continue
                count[nums[j]] -= 1

                # here we have two sum II, where we have a sorted array and find unique combinations
                total = target - nums[j] - nums[i]
                l = j+1
                r = len(nums)-1
                while l<r:
                    if j+1<=l-1<len(nums) and nums[l-1] == nums[l]:
                        l += 1
                        continue
                    summary = nums[l] + nums[r]
                    if summary == total:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                    elif summary < total:
                        l += 1
                    elif summary > total:
                        r -= 1
                
        return res


