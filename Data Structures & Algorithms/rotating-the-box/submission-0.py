class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        # we first move, then rotate

        # for the move, we scan from right to left

        for row in boxGrid:
            right = len(row)-1
            for i in range(len(row)-1, -1, -1):
                if row[i] == "*":
                    right = i - 1
                elif row[i] == "#":
                    row[i] = "."
                    row[right] = "#"
                    right -= 1
        rotateGrid = [["."]*len(boxGrid) for _ in range(len(boxGrid[0]))]
        
        for r in range(len(boxGrid)):
            for c in range(len(boxGrid[0])):
                rotateGrid[c][len(boxGrid)-1-r] = boxGrid[r][c]
        
        return rotateGrid
