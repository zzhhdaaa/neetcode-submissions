class Solution:
    def countSubstrings(self, s: str) -> int:
        def singleExpansion(i: int) -> int:
            count = 0
            exp = 0
            while 0<=i-exp<len(s) and 0<=i+exp<len(s) and s[i-exp] == s[i+exp]:
                count += 1
                exp += 1
            
            return count
        
        def doubleExpansion(i: int) -> int:
            count = 0
            exp = 0
            while 0<=i-exp<len(s) and 0<=i+1+exp<len(s) and s[i-exp] == s[i+1+exp]:
                count += 1
                exp += 1
            
            return count
        
        total = 0
        for i in range(len(s)):
            total += singleExpansion(i) + doubleExpansion(i)
        
        return total