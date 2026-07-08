class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x: x[1])

        pool = [] # minheap of: [dest, psgr]
        
        for req, f, t in trips:
            while pool and pool[0][0] <= f:
                dest, psgr = heapq.heappop(pool)
                capacity += psgr
            
            if capacity < req:
                return False
            
            capacity -= req
            heapq.heappush(pool, [t, req])
        
        return True

