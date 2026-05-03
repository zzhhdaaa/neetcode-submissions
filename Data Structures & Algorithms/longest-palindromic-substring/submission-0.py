class Solution:
    def longestPalindrome(self, s: str) -> str:
        # for each c in s, expand out to find the largest palindrome
        # for each s[i],s[i+1], also expand out
        def singleExpansion(i: int) -> str:
            count = 0
            while 0 <= i+count < len(s) and 0 <= i-count < len(s) and s[i+count] == s[i-count]:
                count += 1
            
            return s[i-(count-1):i+(count-1)+1]
        
        def doubleExpansion(i: int) -> str:
            count = 0
            while 0 <= i-count < len(s) and 0 <= i+1+count < len(s) and s[i-count] == s[i+1+count]:
                count += 1
            
            return s[i-(count-1):i+(count-1)+2]
        
        res = ""

        for i in range(len(s)):
            single = singleExpansion(i)
            double = doubleExpansion(i)
            if len(single) > len(res):
                res = single
            if len(double) > len(res):
                res = double
        
        return res