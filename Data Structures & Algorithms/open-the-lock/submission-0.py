class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # 0 1 2 3 4 5 6 7 8 9
        # _       _
        # 0 1 2 3 4 5 6 7 8 9
        # _       _
        # 0 1 2 3 4 5 6 7 8 9
        # _       _
        # 0 1 2 3 4 5 6 7 8 9
        # _       _

        # at each step, we have 8 choices, representing 4 digits going up or down
        # to find the shortest path, we may wanna use bfs

        queue = deque()
        queue.append(['0000', 0])
        deadends = set(deadends)
        visit = set()
        
        while queue:
            curr, step = queue.popleft()

            if curr in visit:
                continue
            visit.add(curr)

            if curr in deadends:
                continue
            
            if curr == target:
                return step

            up_0 = str((int(curr[0])+1)%10) + curr[1:4]
            up_1 = curr[0:1] + str((int(curr[1])+1)%10) + curr[2:4]
            up_2 = curr[0:2] + str((int(curr[2])+1)%10) + curr[3:4]
            up_3 = curr[0:3] + str((int(curr[3])+1)%10)
            down_0 = str((int(curr[0])+9)%10) + curr[1:4]
            down_1 = curr[0:1] + str((int(curr[1])+9)%10) + curr[2:4]
            down_2 = curr[0:2] + str((int(curr[2])+9)%10) + curr[3:4]
            down_3 = curr[0:3] + str((int(curr[3])+9)%10)

            queue.append([up_0, step+1])
            queue.append([up_1, step+1])
            queue.append([up_2, step+1])
            queue.append([up_3, step+1])
            queue.append([down_0, step+1])
            queue.append([down_1, step+1])
            queue.append([down_2, step+1])
            queue.append([down_3, step+1])
        
        return -1