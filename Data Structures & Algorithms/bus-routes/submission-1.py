class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        
        # we want to create connections between routes, then we do bfs to find the target
        stops = defaultdict(list) # key is stop, value is routes that can reach the stop
        queue = deque() # the queue stores the [idx of routes, bus count]
        visit = set()

        for i in range(len(routes)):
            for stop in routes[i]:
                stops[stop].append(i)
                if stop == source:
                    queue.append([i, 1])
        
        while queue:
            i, count = queue.popleft()

            if i in visit:
                continue
            visit.add(i)

            for stop in routes[i]:
                if stop == target:
                    return count
                for dirc in stops[stop]:
                    if dirc not in visit:
                        queue.append([dirc, count+1])
        
        return -1

