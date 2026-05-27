class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        connections = defaultdict(set)

        for [a,b] in edges:
            connections[a].add(b)
            connections[b].add(a)
        
        # 1: 2,3,4
        # 2: 1
        # 3: 1,4
        # 4: 1,3,5
        # 5: 4

        queue = deque()
        for k in connections:
            if len(connections[k]) == 1:
                queue.append(k)
        
        while queue:
            k = queue.popleft()

            for v in connections[k]:
                connections[v].remove(k)
                if len(connections[v]) == 1:
                    queue.append(v)
            
            connections.pop(k)

        # now, the remaining are removable connections
        for i in range(len(edges)-1, -1, -1):
            a, b = edges[i][0], edges[i][1]
            if a in connections and b in connections[a]:
                return [a,b]
