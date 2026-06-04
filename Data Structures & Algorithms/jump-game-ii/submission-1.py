class Solution:
    def jump(self, nums: List[int]) -> int:
        queue = deque()
        queue.append([0, nums[0], 0]) # curr pos, curr num, step
        visit = set()
        visit.add(0)
        while queue:
            pos, num, step = queue.popleft()

            if pos == len(nums)-1:
                return step

            for j in range(len(nums)-1, pos, -1):
                if j-pos <= num and j not in visit:
                    queue.append([j, nums[j], step+1])
                    visit.add(j)

        return -1