class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def To2D(num: int):
            i = num // len(matrix[0])
            j = num % len(matrix[0])
            return i, j
        
        def To1D(i: int, j: int):
            return i*len(matrix[0])+j
        
        def binary_search(l: int, r: int) -> bool:
            if l > r:
                return False
            
            m = l + (r - l) // 2
            i, j = To2D(m)

            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                return binary_search(m+1, r)
            else:
                return binary_search(l, m-1)
        
        return binary_search(0, len(matrix)*len(matrix[0])-1)
            
            