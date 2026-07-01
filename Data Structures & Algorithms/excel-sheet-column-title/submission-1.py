class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        mapping = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        res = []
        while columnNumber:
            columnNumber -= 1
            mod = columnNumber % 26
            res.append(mapping[mod])
            columnNumber //= 26
        
        return ''.join(reversed(res))