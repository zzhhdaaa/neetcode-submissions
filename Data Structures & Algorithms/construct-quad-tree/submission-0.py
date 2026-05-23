"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        root = Node()

        def dfs(node: Node, subGrid: List[List[int]]):
            # topLeft -> row cornerTL[0]:(cornerTL[0]+cornerBR[0])//2
            #         -> col cornerTL[1]:(cornerTL[1]+cornerBR[1])//2
            if len(subGrid) == 1:
                node.val = subGrid[0][0]
                node.isLeaf = True
                return
            
            TL = [0, 0]
            BR = [len(subGrid), len(subGrid)]
            TLgrid = [row[TL[1]:(TL[1]+BR[1])//2] for row in subGrid[TL[0]:(TL[0]+BR[0])//2]]
            TRgrid = [row[(TL[1]+BR[1])//2:BR[1]] for row in subGrid[TL[0]:(TL[0]+BR[0])//2]]
            BLgrid = [row[TL[1]:(TL[1]+BR[1])//2] for row in subGrid[(TL[0]+BR[0])//2:BR[0]]]
            BRgrid = [row[(TL[1]+BR[1])//2:BR[1]] for row in subGrid[(TL[0]+BR[0])//2:BR[0]]]
            
            isLeaf = True
            val = TLgrid[0][0]
            for r in range(len(TLgrid)):
                for c in range(len(TLgrid)):
                    if TLgrid[r][c] == TRgrid[r][c] == BLgrid[r][c] == BRgrid[r][c] == val:
                        continue
                    else:
                        isLeaf = False
                        val = 1
                        break
                if not isLeaf:
                    break
            
            if not isLeaf:
                node.val = val
                node.isLeaf = False
                node.topLeft = Node()
                dfs(node.topLeft, TLgrid)
                node.topRight = Node()
                dfs(node.topRight, TRgrid)
                node.bottomLeft = Node()
                dfs(node.bottomLeft, BLgrid)
                node.bottomRight = Node()
                dfs(node.bottomRight, BRgrid)
            else:
                node.val = val
                node.isLeaf = True
        
        dfs(root, grid)
        return root