class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False
        
        ptr1, ptr2 = 0, 0
        memo = dict()

        def backtrack(ptr3: int):
            nonlocal ptr1, ptr2
            if ptr3 >= len(s3):
                return True
            
            key = (ptr1, ptr2, ptr3)
            if key in memo:
                return memo[key]
            
            res = False
            if ptr1 < len(s1) and s1[ptr1] == s3[ptr3]:
                ptr1 += 1
                res = res or backtrack(ptr3 + 1)
                ptr1 -= 1
            if res:
                memo[key] = True
                return True

            if ptr2 < len(s2) and s2[ptr2] == s3[ptr3]:
                ptr2 += 1
                res = res or backtrack(ptr3 + 1)
                ptr2 -= 1
            memo[key] = res
            return res
        
        return backtrack(0)