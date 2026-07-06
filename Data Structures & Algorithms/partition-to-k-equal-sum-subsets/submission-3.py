class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)

        if total%k != 0:
            return False
        target = total//k
        visit = [0 for _ in range(len(nums))]
        nums.sort(reverse=True)
        if nums[0] > target:
            return False
        memo = dict()

        def backtrack(i: int, subsum: int) -> bool: # the ith bucket, curr sum
            if i >= k-1: # if we successfully formed k-1 buckets, the remaining one auto succeed
                return True
            
            if subsum == target:
                return backtrack(i+1, 0)
            
            key = (tuple(visit), i, subsum)
            if key in memo:
                return memo[key]
            
            # add any possible number to the subsum
            prev = -1 # avoid adding same value to subset
            for n in range(len(nums)):
                if visit[n] == 1 or nums[n] + subsum > target or nums[n] == prev:
                    continue
                
                visit[n] = 1
                
                if backtrack(i, subsum + nums[n]):
                    return True
                
                visit[n] = 0
                prev = nums[n]

                if subsum == 0:
                    memo[key] = False
                    return False
            
            memo[key] = False
            return False
        
        return backtrack(0, 0)
            
            