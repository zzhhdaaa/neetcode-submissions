class Solution:
    def reverse(self, x: int) -> int:
        MIN = -2147483648  # -2^31,
        MAX = 2147483647  #  2^31 - 1

        POS = x >= 0
        x = abs(x)
        res = 0
        while x:
            mod = x % 10
            x = x // 10
            if POS and (res > MAX // 10 or (res == MAX // 10 and mod > MAX % 10)):
                return 0
            if not POS and (-res < MIN // 10 or (-res == MIN // 10 and mod < MIN % 10)):
                return 0
            res = res*10 + mod
        
        return res if POS else -res