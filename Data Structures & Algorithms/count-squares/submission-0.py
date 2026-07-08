class CountSquares:

    def __init__(self):
        self.grid = [[0 for _ in range(1001)] for _ in range(1001)] # the count of (x,y)
        self.xcount = [0] * 1001
        self.ycount = [0] * 1001

    def add(self, point: List[int]) -> None:
        self.grid[point[0]][point[1]] += 1
        self.xcount[point[0]] += 1
        self.ycount[point[1]] += 1

    def count(self, point: List[int]) -> int:
        x0, y0 = point[0], point[1]

        if self.xcount[point[0]] == 0 or self.ycount[point[1]] == 0:
            return 0
        
        res = 0
        for y1 in range(1001):
            # we scan through the same x axis as point
            # point0: x0, y0
            # point1: x0, y1
            # point2: x1, y1 (x1 = x0 - edge or x0 + edge)
            # point3: x1, y0
            if self.grid[x0][y1] == 0 or y1 == y0:
                continue
            edge = abs(y0-y1)

            x1 = x0 - edge
            if x1 >= 0:
                res += self.grid[x0][y1] * self.grid[x1][y1] * self.grid[x1][y0]
            
            x1 = x0 + edge
            if x1 <= 1000:
                res += self.grid[x0][y1] * self.grid[x1][y1] * self.grid[x1][y0]
        
        return res
