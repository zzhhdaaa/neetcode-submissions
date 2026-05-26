class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # binary search for the target dest
        l = 0
        r = len(arr) - 1

        while l<r:
            m = (l+r)//2

            if arr[m] < x:
                l = m+1
            else:
                r = m
        
        # now, we start from l and spread out, the final outcome would be arr[l:r+1]
        l = l-1
        r = l+1
        while r-l < k+1:
            if l < 0:
                r += 1
            elif r >= len(arr):
                l -= 1
            elif abs(arr[l]-x) <= abs(arr[r]-x):
                l -= 1
            else:
                r += 1
        
        return arr[l+1:r]