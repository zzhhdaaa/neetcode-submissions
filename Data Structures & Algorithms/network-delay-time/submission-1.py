class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        nodes = defaultdict(list)

        for u, v, t in times:
            nodes[u].append([t, v])
        
        visit = dict()
        minheap = []
        heapq.heappush(minheap, [0, k]) # weight, node
        time = 0

        while minheap:
            weight, node = heapq.heappop(minheap)

            if node in visit:
                continue
            visit[node] = weight
            time = max(time, weight)

            for w, d in nodes[node]: # w = weight, d = dest
                minheap.append([weight+w, d])
            heapq.heapify(minheap)
        
        return time if len(visit) == n else -1

