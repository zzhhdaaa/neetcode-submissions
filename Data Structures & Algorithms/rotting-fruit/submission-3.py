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
            directions = [[0,1],[0,-1],[1,0],[-1,0]]
            # rot the surroundings base on the centre
            for dr, dc in directions:
                if r+dr in range(ROW) and c+dc in range(COL)\
                    and grid[r+dr][c+dc] == 1:
                    grid[r+dr][c+dc] = 2
                    fresh -= 1
                    q.append([r+dr, c+dc])
        
        result = 0
        while q and fresh != 0:
            count = len(q)
            prevFresh = fresh
            for i in range(count):
                r, c = q.popleft()
                rot(r, c)
            result += 1 if fresh != prevFresh else 0
        
        return -1 if fresh != 0 else result
