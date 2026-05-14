class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #   0
        #  /｜\
        # 1 2 3
        # |
        # 4

        #      0
        #      |
        #      1
        #   /  |  \
        #  2 - 3   4
        if n == 1:
            return len(edges) == 0

        edgeMap = defaultdict(list)

        for a,b in edges:
            edgeMap[a].append(b)
            edgeMap[b].append(a)
        
        # to check if a tree has loop, use dfs + visit set
        visit = set()
        def dfs(node: int, prev: int):
            if node in visit:
                return True
            
            visit.add(node)

            flag = False
            for dest in edgeMap[node]:
                if dest != prev:
                    flag = dfs(dest, node) or flag
            return flag
        
        return not dfs(edges[0][0], "") and len(visit) == len(edgeMap.keys())
