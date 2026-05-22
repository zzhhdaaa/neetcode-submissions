class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # we do the rotation layer by layer
        # one layer means a circle outside
        N = len(matrix)

        def rotate_layer(layer: int):
            # [0,0] -> [0,N-1] -> [N-1,N-1] -> [N-1,0] -> [0,0]
            # [0,1] -> [1,N-1] -> [N-1,1] -> [1,0] -> [0,1]
            for i in range(N-1-2*layer):
                print(layer)
                print([layer, layer+i], [N-1-layer-i, layer], [N-1-layer, N-1-layer-i], [layer+i, N-1-layer])
                tmp = matrix[layer][layer+i]
                matrix[layer][layer+i] = matrix[N-1-layer-i][layer]
                matrix[N-1-layer-i][layer] = matrix[N-1-layer][N-1-layer-i]
                matrix[N-1-layer][N-1-layer-i] = matrix[layer+i][N-1-layer]
                matrix[layer+i][N-1-layer] = tmp

        for layer in range(N//2):
            rotate_layer(layer)