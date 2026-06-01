class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_map = defaultdict(int)
        task_heap = [] 

        for task in tasks:
            task_map[task] += 1
        
        for task in task_map.keys():
            heapq.heappush_max(task_heap, task_map[task])

        res = 0
        while len(task_heap) != 0:
            temp = []
            cycle = n+1

            for _ in range(cycle):
                if not (len(temp)==0 and len(task_heap)==0):
                    res += 1
                if task_heap:
                    task = heapq.heappop_max(task_heap)
                    task -= 1
                    if task != 0:
                        temp.append(task)
            
            for t in temp:
                heapq.heappush_max(task_heap, t)
        
        return res

