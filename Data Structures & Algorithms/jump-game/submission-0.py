class Solution:
    def canJump(self, nums: List[int]) -> bool:
        queue = deque()
        queue.append([0, nums[0]]) # idx, maxjump
        visit = set()
        visit.add(0)
        while queue:
            idx, maxjump = queue.popleft()

            if idx == len(nums) - 1:
                return True

            # jump forward
            for i in range(idx+1, min(len(nums), idx+1+maxjump)):
                if i not in visit:
                    queue.append([i, nums[i]])
        
        return False
