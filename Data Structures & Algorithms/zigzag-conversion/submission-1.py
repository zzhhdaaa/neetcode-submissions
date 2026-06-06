class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # G    I    N <- this row = i%numRows
        # O  E S  I G
        # O L  H R
        # G    I
        if numRows == 1 or len(s) == 1:
            return s


        rows = [[] for _ in range(numRows)]

        for i in range(len(s)):
            row = i%(2*numRows-2)
            if row+1 > numRows:
                row = 2*numRows-2-row
            rows[row].append(s[i])
        
        
        return "".join("".join(row) for row in rows)