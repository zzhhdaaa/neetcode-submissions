class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dict_s = dict()

        for c in s:
            if c in dict_s.keys():
                dict_s[c] += 1
            else:
                dict_s[c] = 1
        
        for c in t:
            if c not in dict_s.keys():
                return False
            else:
                dict_s[c] -= 1
            
            if dict_s[c] < 0:
                return False
        
        for count in dict_s.values():
            if count != 0:
                return False
        
        return True