class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque() # each item is [idx, val]
        
        res = []
        for i in range(0, len(nums)):
            right = i
            left = i-k+1

            # maintain the decreasing val order of the queue
            while queue and queue[-1][1] < nums[right]:
                queue.pop()
            queue.append([right, nums[right]])

            if left < 0:
                continue
            
            # take the result
            res.append(queue[0][1])

            # remove the left for the next
            if queue[0][0] <= left:
                queue.popleft()
        
        return res

