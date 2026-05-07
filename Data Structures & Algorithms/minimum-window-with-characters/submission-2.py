class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = dict()
        total = 0 # total type of char to be satisfied

        for c in t:
            if c in count:
                count[c] += 1
            else:
                count[c] = 1
                total += 1
        
        # OUZODYXAZV, XYZ
        #      _  _

        # l, r: left idx and right idx, inclusive
        r = 0
        res = ""

        # when a char count turns from 1 to 0, total -1
        # when a char count turns from 0 to 1, total +1
        # only when total == 0 means the curr(s[l:r]) satisfied the condition

        for l in range(len(s)):
            # curr = s[l:r] # this is the curr substring, starting from ""

            while total > 0 and r < len(s): # when not satisfying
                added = s[r] # we add the r pointing char into the window
                if added in count:
                    count[added] -= 1
                    if count[added] == 0: # when a char count turns from 1 to 0, that char satisfied
                        total -= 1
                r += 1
            
            # now, the above potentially makes sure the curr satisfied the requirements
            if total == 0:
                curr = s[l:r]
                if res == "":
                    res = curr
                elif len(curr) <= len(res):
                    res = curr
                
                # we remove the current l pointing char
                removed = s[l]
                if removed in count:
                    count[removed] += 1
                    if count[removed] == 1: # when a char count turns from 0 to 1, that char disatisfied
                        total += 1
        
        return res
                