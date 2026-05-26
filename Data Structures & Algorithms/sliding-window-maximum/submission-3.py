class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque() # each item is [idx, val]
        
        # prefill values for the first window
        for i in range(k-1):
            num = nums[i]
            while queue and queue[0][1] <= num:
                queue.popleft()
            queue.append([i, num])
        
        res = []
        for i in range(k-1, len(nums)):
            right = i
            left = i-k+1

            # maintain the largest value at left
            while queue and queue[0][1] <= nums[right]:
                queue.popleft()
            # maintain the second largest value at right
            while len(queue)>=2 and queue[-1][1] <= nums[right]:
                queue.pop()
            queue.append([right, nums[right]])

            print(left, right)
            print(queue)

            # take the result
            res.append(queue[0][1])

            # remove the left for the next
            if queue[0][0] <= left:
                queue.popleft()
        
        return res

