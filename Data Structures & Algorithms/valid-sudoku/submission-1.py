class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rols = [dict() for _ in range(len(board))]
        cols = [dict() for _ in range(len(board))]
        grids = [dict() for _ in range(len(board))]

        print(rols)

        for i in range(len(board)):
            for j in range(len(board[i])):
                item = board[i][j]

                if item == ".":
                    continue
                
                rols[i][item] = rols[i].get(item, 0) + 1
                cols[j][item] = cols[j].get(item, 0) + 1
                grids[i//3*3 + j//3][item] = grids[i//3*3 + j//3].get(item, 0) + 1
                
                if rols[i][item] > 1 or cols[j][item] > 1 or grids[i//3*3 + j//3][item] > 1:
                    return False
        
        return True

