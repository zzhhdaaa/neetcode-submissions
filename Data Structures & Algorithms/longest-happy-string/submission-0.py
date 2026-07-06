class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # greedy -> always take the most rest
        heap = []
        if a > 0: heapq.heappush_max(heap, [a, 'a'])
        if b > 0: heapq.heappush_max(heap, [b, 'b'])
        if c > 0: heapq.heappush_max(heap, [c, 'c'])
        
        res = []

        while heap:
            topcount, top = heapq.heappop_max(heap)

            # the top is working
            if not (len(res) >= 2 and res[-1] == top and res[-2] == top):
                res.append(top)
                if topcount-1 > 0:
                    heapq.heappush_max(heap, [topcount-1, top])
                continue
            
            # get the mid
            if len(heap) == 0:
                continue
            midcount, mid = heapq.heappop_max(heap)

            # the mid is guaranteed working if the top is not working
            if not (len(res) >= 2 and res[-1] == mid and res[-2] == mid):
                res.append(mid)
                if midcount-1 > 0:
                    heapq.heappush_max(heap, [midcount-1, mid])
                heapq.heappush_max(heap, [topcount, top])
                continue
        
        return "".join(res)
