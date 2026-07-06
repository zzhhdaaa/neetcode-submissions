class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        a, b = str1, str2

        if len(a) > len(b):
            b, a = a, b
        # now a is always the shorter one

        for n in range(len(a), 0, -1):
            if len(a)%n == 0 and len(b)%n == 0:
                s = a[0:n]
                if s*(len(a)//n)==a and s*(len(b)//n)==b:
                    return s
        
        return ""