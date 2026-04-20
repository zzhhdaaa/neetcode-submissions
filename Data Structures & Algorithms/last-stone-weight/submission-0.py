class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []

        for stone in stones:
            heapq.heappush(maxHeap, -stone)

        while len(maxHeap) > 1:
            x = -heapq.heappop(maxHeap)
            y = -heapq.heappop(maxHeap)
            diff = abs(x-y)

            if diff != 0:
                heapq.heappush(maxHeap, -diff)
        
        return 0 if len(maxHeap) == 0 else -heapq.heappop(maxHeap)
