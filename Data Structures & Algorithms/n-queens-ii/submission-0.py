class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        dias = set() # r+c
        revs = set() # r-c

        res = 0
        def backtrack(row: int):
            nonlocal res
            if row >= n:
                res += 1
                return
            
            for col in range(n):
                dia = row + col
                rev = row - col
                if col not in cols and dia not in dias and rev not in revs:
                    cols.add(col)
                    dias.add(dia)
                    revs.add(rev)

                    backtrack(row+1)

                    cols.remove(col)
                    dias.remove(dia)
                    revs.remove(rev)
        
        backtrack(0)
        return res