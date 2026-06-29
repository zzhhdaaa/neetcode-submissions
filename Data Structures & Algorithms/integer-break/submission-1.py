class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        elif n == 3:
            return 2
        elif n == 4:
            return 4
        
        mod = n%3
        power = n//3

        if mod == 1:
            return 3**(power-1) * 4
        elif mod == 2:
            return 3**power * 2
        
        return 3**power