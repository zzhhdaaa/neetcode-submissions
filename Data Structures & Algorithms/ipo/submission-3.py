class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        available = [] # maxheap according to the profits, only store available
        waiting = [] # minheap according to the require capital, only store unavailable

        for i in range(len(profits)):
            if capital[i] <= w:
                heapq.heappush_max(available, profits[i])
            else:
                heapq.heappush(waiting, [capital[i], i])
        
        for _ in range(k):
            if available:
                pro = heapq.heappop_max(available)
                w += pro
            while waiting and w >= waiting[0][0]:
                cap, idx = heapq.heappop(waiting)
                pro = profits[idx]
                heapq.heappush_max(available, pro)
        
        return w