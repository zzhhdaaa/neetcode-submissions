class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        distance = dict()
        for point in points:
            x = point[0]
            y = point[1]
            d = math.sqrt(x*x + y*y)
            heapq.heappush(minHeap, d)
            if d not in distance.keys():
                distance[d] = [point]
            else:
                distance[d].append(point)
        
        print(distance)
        result = []
        for i in range(k):
            result.append(distance[heapq.heappop(minHeap)].pop())
        
        return result

