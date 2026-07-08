class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        edges = dict()

        for f, t in tickets:
            if f not in edges:
                edges[f] = dict()
                edges[f][t] = 1
            else:
                edges[f][t] = edges[f].get(t, 0) + 1
        
        res = None
        curr = ["JFK"]
        def dfs(f: str):
            # already done the first construction
            nonlocal res
            if res:
                return
            
            # reach end, store to res
            if len(curr) == len(tickets)+1:
                res = curr.copy()
                return
            
            # no possible next target
            if f not in edges:
                return
            possible = False
            for t in edges[f].keys():
                if edges[f][t] == 0:
                    continue
                edges[f][t] -= 1
                curr.append(t)
                dfs(t)
                edges[f][t] += 1
                curr.pop()
        
        dfs("JFK")
        return res