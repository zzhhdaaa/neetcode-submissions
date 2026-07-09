class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x//2 + 1

        while l < r:
            m = (l+r)//2

            a = m*m
            b = (m+1)*(m+1)

            if a <= x and b > x:
                return m
            elif a > x:
                r = m
            elif b <= x:
                l = m + 1
        
        return l