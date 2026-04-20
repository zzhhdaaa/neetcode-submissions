class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = 0
        prefix = ""

        while pre < len(strs[0]):
            c = strs[0][pre]
            for s in strs:
                if pre > len(s) - 1:
                    return prefix
                if s[pre] != c:
                    return prefix
            pre = pre + 1
            prefix = prefix + c
        
        return prefix

