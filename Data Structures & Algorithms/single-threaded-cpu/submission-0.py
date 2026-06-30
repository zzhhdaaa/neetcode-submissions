class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        waiting = [] # the waiting ones, prioritized by enqueue time
        working = [] # the available ones, prioritized by process time

        for i in range(len(tasks)):
            tasks[i].append(i)
            heapq.heappush(waiting, tasks[i])
        
        time = 0
        res = []

        print(working or waiting)

        while working or waiting:
            # work
            if working:
                process, idx = heapq.heappop(working)
                time += process
                res.append(idx)

            # add new ones to working if possible
            if waiting and time < waiting[0][0] and not working:
                # skip and advance time
                time = waiting[0][0]
            while waiting and time >= waiting[0][0]:
                enqueue, process, idx = heapq.heappop(waiting)
                heapq.heappush(working, [process, idx])
        
        return res