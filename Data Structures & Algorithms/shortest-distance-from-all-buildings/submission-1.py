class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        # key is the "0" location, value is {key is "1" location, value is distance}
        distance = defaultdict(dict)
        buildings = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    buildings += 1
                    queue = deque()
                    queue.append([i,j,0])
                    seen = set()
                    while queue:
                        row, col, dis = queue.popleft()
                        if (row, col) in seen:
                            continue
                        seen.add((row, col))
                        if row<0 or row>=len(grid) or col<0 or col>=len(grid[0]):
                            continue
                        if grid[row][col] == 0:
                            distance[(row,col)][(i,j)] = dis
                        if grid[row][col] == 0 or dis == 0:
                            queue.append([row-1,col,dis+1])
                            queue.append([row+1,col,dis+1])
                            queue.append([row,col-1,dis+1])
                            queue.append([row,col+1,dis+1])
        
        minDis = float('inf')
        for dis_to_buildings in distance.values():
            if len(dis_to_buildings.keys()) == buildings:
                sumDis = sum(dis_to_buildings.values())
                minDis = min(minDis, sumDis)
        
        if minDis != float('inf'):
            return minDis
        return -1
                        
