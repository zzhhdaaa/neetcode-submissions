class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = defaultdict(set)
        reverseMap = defaultdict(set)

        for [a, b] in prerequisites:
            preMap[a].add(b)
            reverseMap[b].add(a)
        
        queue = deque()
        # we only keep the already solved courses in the queue, and solve bottom-up
        for c in range(numCourses):
            if c not in preMap:
                queue.append(c)
        
        res = []
        while queue:
            c = queue.popleft()

            # already solved, just append
            res.append(c)
            if c not in reverseMap:
                # no one relies on c
                continue
            
            for n in reverseMap[c]:
                # the n course that requires c
                preMap[n].remove(c)
                if len(preMap[n]) == 0:
                    # n is solved
                    queue.append(n)
        
        if len(res) != numCourses:
            return []
        return res

