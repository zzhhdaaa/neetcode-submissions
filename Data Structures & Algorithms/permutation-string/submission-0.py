class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # s2: lecabee
        #      ---
        # s1: abc

        if len(s1) > len(s2):
            return False

        s1dict = dict()
        s2dict = dict()

        for c in s1:
            s1dict[c] = s1dict.get(c, 0) + 1
        
        for i in range(len(s2)):
            s2dict[s2[i]] = s2dict.get(s2[i], 0) + 1
            if i >= len(s1):
                s2dict[s2[i-len(s1)]] -= 1
                if s2dict[s2[i-len(s1)]] == 0:
                    s2dict.pop(s2[i-len(s1)])
            if s1dict == s2dict:
                return True
        
        return False
