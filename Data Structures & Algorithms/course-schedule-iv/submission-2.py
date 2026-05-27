class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        course_to_pre = defaultdict(set)
        for [a, b] in prerequisites:
            course_to_pre[b].add(a)
        
        memo = dict()
        def dfs(u: int, v: int) -> bool: # is u a prerequisite of v?
            if v not in course_to_pre:
                # v has no prerequisite at all
                return False
            
            if u in course_to_pre[v]:
                # if u is v's direct prerequisite
                return True
            
            if (u,v) in memo:
                return memo[(u,v)]
            # continue search down for indirect prerequisite
            flag = False
            for pre in course_to_pre[v]:
                flag = flag or dfs(u, pre)
            if flag:
                course_to_pre[v].add(u)
            memo[(u,v)] = flag
            return flag

        res = []
        for [u, v] in queries:
            res.append(dfs(u, v))
        
        return res


            
        
