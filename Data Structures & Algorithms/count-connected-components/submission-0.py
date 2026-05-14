class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        edgeMap = defaultdict(list)

        for a,b in edges:
            edgeMap[a].append(b)
            edgeMap[b].append(a)

        visit = set()
        res = 0
        def dfs(i: int, prev: int):
            if i in visit:
                return False
            visit.add(i)
            
            if i not in edgeMap:
                print("single node tree")
                return True
            
            for dest in edgeMap[i]:
                if dest != prev:
                    dfs(dest, i)
            return True
        
        for i in range(n):
            res += 1 if dfs(i, i) else 0
        return res
