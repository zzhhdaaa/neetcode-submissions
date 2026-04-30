class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # key: the course, value: the prerequisites set
        pre_map = defaultdict(set)
        for pre in prerequisites:
            if pre[0] == pre[1]:
                return False
            pre_map[pre[0]].add(pre[1])
        
        seen = set()
        def dfs(i: int) -> bool:
            if i in seen:
                return False

            if i not in pre_map:
                return True
            
            seen.add(i)
            
            for pre in pre_map[i]:
                if not dfs(pre):
                    return False
            
            seen.remove(i)
            pre_map.pop(i) # for those already solved, marked as solvable, avoid future search
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True