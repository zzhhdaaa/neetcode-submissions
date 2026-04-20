class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        results = dict() # the key is the diff between target and num, the value is a list of indices
        for i in range(len(nums)):
            diff = target - nums[i]
            if nums[i] not in results.keys():
                results[diff] = [i]
            else:
                results[nums[i]].append(i)
                return results[nums[i]]
        return []