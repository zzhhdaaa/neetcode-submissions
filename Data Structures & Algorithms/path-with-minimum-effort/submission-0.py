class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # dijkstra
        ROW, COL = len(heights), len(heights[0])
        heap = []
        heapq.heappush(heap, [0, 0, 0]) # effort, row, col
        visit = set()

        while heap:
            effort, row, col = heapq.heappop(heap)

            if row==ROW-1 and col==COL-1:
                return effort

            if (row, col) in visit:
                continue
            visit.add((row, col))

            if row-1>=0 and (row-1,col) not in visit:
                neweffort = abs(heights[row][col]-heights[row-1][col])
                heapq.heappush(heap, [max(effort, neweffort), row-1, col])
            if col-1>=0 and (row,col-1) not in visit:
                neweffort = abs(heights[row][col]-heights[row][col-1])
                heapq.heappush(heap, [max(effort, neweffort), row, col-1])
            if row+1<ROW and (row+1,col) not in visit:
                neweffort = abs(heights[row][col]-heights[row+1][col])
                heapq.heappush(heap, [max(effort, neweffort), row+1, col])
            if col+1<COL and (row,col+1) not in visit:
                neweffort = abs(heights[row][col]-heights[row][col+1])
                heapq.heappush(heap, [max(effort, neweffort), row, col+1])

