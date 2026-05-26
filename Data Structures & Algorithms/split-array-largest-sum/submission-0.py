class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # we can do dfs. it would be a 2^n time. potentially reduce it by using memo
        # instead we can also binary search for the max output
        # the question becomes:
        # what is the smallest capacity for nums to be splitted into k subarrays

        l = 1
        r = sum(nums)

        def can_split(cap: int):
            curr = cap
            res = 1
            for num in nums:
                if num > cap:
                    return False
                if num <= curr:
                    curr -= num
                else:
                    curr = cap - num
                    res += 1
            return res <= k

        while l<r:
            m = (l+r)//2

            if can_split(m):
                r = m
            else:
                l = m + 1
        
        return l
