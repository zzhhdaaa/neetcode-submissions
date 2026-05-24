class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROW = len(board)
        COL = len(board[0])
        visit = set()

        def dfs(r: int, c: int, root: bool, island: set):
            if not 0<=r<ROW or not 0<=c<COL:
                return False
            
            if board[r][c] == 'X' or board[r][c] == 'P':
                return True
            
            # continue checking, placing P as pending mark
            board[r][c] = 'P'
            surrounded = dfs(r+1,c,False,island) and dfs(r-1,c,False,island) and dfs(r,c+1,False,island) and dfs(r,c-1,False,island)
            if surrounded and root:
                for (row,col) in island:
                    board[row][col] = 'X'
            elif surrounded and not root:
                island.add((r,c))
            elif not surrounded and root:
                for (row,col) in island:
                    board[row][col] = 'O'
            elif not surrounded and not root:
                board[r][c] = 'O'
            visit.add((r,c))
            return surrounded
        
        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == 'O' and (r,c) not in visit:
                    dfs(r,c,True,{(r,c)})
