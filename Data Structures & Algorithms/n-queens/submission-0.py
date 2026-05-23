class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # any two queens cannot appear in the same row, col, posdiag, negdiag
        # row = set() # r
        cols = set() # c
        posDiags = set() # r+c
        negDiags = set() # r-c
        base = "." * n

        res = []
        curr = []

        def placeQueen(r: int, c: int):
            # check current validation
            if c in cols or r+c in posDiags or r-c in negDiags:
                return
            
            # ending and passed validation, append to result
            if r == n-1:
                curr.append(base[:c] + "Q" + base[c+1:])
                res.append(curr.copy())
                curr.pop()
                return

            # haven't ended yet
            cols.add(c)
            posDiags.add(r+c)
            negDiags.add(r-c)
            curr.append(base[:c] + "Q" + base[c+1:])

            # continue to next row
            for col in range(n):
                placeQueen(r+1, col)
            
            cols.remove(c)
            posDiags.remove(r+c)
            negDiags.remove(r-c)
            curr.pop()

        # iterate through each row, since each row can only place one queen
        for col in range(n):
            placeQueen(0, col)
        
        return res


