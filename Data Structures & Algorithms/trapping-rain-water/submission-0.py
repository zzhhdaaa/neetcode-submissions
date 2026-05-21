class Solution:
    def trap(self, height: List[int]) -> int:
        LEN = len(height)
        lmax = [0] * LEN # for each slots, what the left cap of it would be (including self)
        rmax = [0] * LEN

        currlmax = 0
        currrmax = 0
        for i in range(LEN):
            currlmax = max(currlmax, height[i])
            currrmax = max(currrmax, height[LEN-1-i])
            lmax[i] = currlmax
            rmax[LEN-1-i] = currrmax
        
        res = 0
        for i in range(LEN):
            res += min(lmax[i], rmax[i]) - height[i]
        
        return res

