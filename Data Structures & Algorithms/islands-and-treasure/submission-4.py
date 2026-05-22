class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        ROW = len(grid)
        COL = len(grid[0])

        treasures = []
        # we find each treasure first, then spread out
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    treasures.append([r,c])

        # we start at all treasure location
        queue = deque()
        for treasure in treasures:
            queue.append([treasure[0], treasure[1], 0])
        visit = set()

        while queue:
            row, col, dis = queue.popleft()
            
            # out of bound or water or chest
            if not 0<=row<ROW or not 0<=col<COL or grid[row][col] == -1:
                continue
            
            # check visit
            if (row, col) in visit:
                continue
            visit.add((row,col))

            # update the min distance
            grid[row][col] = min(grid[row][col], dis)

            # spread out
            queue.append([row+1,col,dis+1])
            queue.append([row-1,col,dis+1])
            queue.append([row,col+1,dis+1])
            queue.append([row,col-1,dis+1])
        
        
