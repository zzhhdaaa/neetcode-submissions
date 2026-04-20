class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # we want to do a breadth first search
        # first, we put all the rotten ones into a queue
        q = deque()
        fresh = 0
        ROW, COL = len(grid), len(grid[0])
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 2:
                    q.append([r,c])
                elif grid[r][c] == 1:
                    fresh += 1
        
        def rot(r: int, c: int):
            nonlocal q
            nonlocal fresh
            # rot the surroundings base on the centre
            if r-1 in range(ROW) and grid[r-1][c] == 1:
                grid[r-1][c] = 2
                q.append([r-1,c])
                fresh -= 1
            if r+1 in range(ROW) and grid[r+1][c] == 1:
                grid[r+1][c] = 2
                q.append([r+1,c])
                fresh -= 1
            if c-1 in range(COL) and grid[r][c-1] == 1:
                grid[r][c-1] = 2
                q.append([r,c-1])
                fresh -= 1
            if c+1 in range(COL) and grid[r][c+1] == 1:
                grid[r][c+1] = 2
                q.append([r,c+1])
                fresh -= 1
        
        result = 0
        while q and fresh != 0:
            count = len(q)
            prevFresh = fresh
            for i in range(count):
                r, c = q.popleft()
                rot(r, c)
            result += 1 if fresh != prevFresh else 0
        
        return -1 if fresh != 0 else result
