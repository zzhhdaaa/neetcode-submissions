class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # For any subarray in an array, we can represent that as:
        #       [      ] =
        # [            ] -
        # [    ]

        prefixSums = dict()
        prefixSums[0] = 1 # this is for when the current subarray sums directly to k
        tempSum = 0
        count = 0

        for i in range(len(nums)):
            tempSum += nums[i] # 1

            # we wanna check if there's tempSum - prefix = k => prefix = tempSum - k
            prefix = tempSum - k # = 1 - 0 = 1
            count += prefixSums.get(prefix, 0)

            # add the current sum into the prefix for next iteration
            prefixSums[tempSum] = prefixSums.get(tempSum, 0) + 1 # 0: 1, 1: 1
        
        return count