class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0
        res = [0, k]
        for r in range(k, len(arr)):
            l = r-k
            left = abs(arr[l]-x)
            right = abs(arr[r]-x)

            # only update the res to next window when right is closer
            if left > right:
                res = [l+1, r+1]

        return arr[res[0]:res[1]]