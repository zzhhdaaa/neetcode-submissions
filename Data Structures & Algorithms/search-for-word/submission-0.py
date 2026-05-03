class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(row: int, col: int, idx: int) -> bool:
            if not (0<=row<len(board) and 0<=col<len(board[0])):
                return False
            
            if idx == len(word) - 1 and board[row][col] == word[idx]:
                return True
            
            if board[row][col] == word[idx]:
                tmp = board[row][col]
                board[row][col] = "***"
                res = dfs(row+1,col,idx+1) or dfs(row-1,col,idx+1) or dfs(row,col+1,idx+1) or dfs(row,col-1,idx+1)
                board[row][col] = tmp
                return res
            
            return False
        
        found = False
        for i in range(len(board)):
            for j in range(len(board[0])):
                found = found or dfs(i,j,0)
        
        return found
