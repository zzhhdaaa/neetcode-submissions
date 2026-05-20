class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ROW = len(matrix)
        COL = len(matrix[0])
        NUM = ROW * COL

        res = []

        def go_spiral(r: int, c: int, dirt: List[int]):
            if len(res) == NUM:
                return
            
            # out bound or reach previous, turn right
            if not 0<=r<ROW or not 0<=c<COL or matrix[r][c] is None:
                r -= dirt[0]
                c -= dirt[1]
                newDir = [0,0]
                if dirt == [0,1]:
                    newDir = [1,0]
                elif dirt == [1,0]:
                    newDir = [0,-1]
                elif dirt == [0,-1]:
                    newDir = [-1,0]
                elif dirt == [-1,0]:
                    newDir = [0,1]
                
                go_spiral(r+newDir[0], c+newDir[1], newDir)
                return
            
            # ongoing
            res.append(matrix[r][c])
            matrix[r][c] = None
            go_spiral(r+dirt[0], c+dirt[1], dirt)
        
        go_spiral(0, 0, [0,1])
        return res
            
