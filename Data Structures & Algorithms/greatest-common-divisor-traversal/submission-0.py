from math import gcd

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        edges = defaultdict(set)

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if gcd(nums[i], nums[j]) > 1:
                    edges[i].add(j)
                    edges[j].add(i)
        
        if len(edges) != len(nums):
            return False
        
        queue = deque()
        queue.append(0)
        visit = set()
        visit.add(0)

        while queue:
            curr = queue.popleft()

            for target in edges[curr]:
                if target not in visit:
                    queue.append(target)
                    visit.add(target)
        
        return len(visit) == len(nums)