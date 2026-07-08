class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        variables = set()
        edges = defaultdict(set)
        pairs = dict()

        for i in range(len(equations)):
            A, B, val = equations[i][0], equations[i][1], values[i]
            pairs[(A, B)] = val
            edges[A].add(B)
            if val != 0:
                pairs[(B, A)] = 1/val
                edges[B].add(A)
            variables.add(A)
            variables.add(B)
        print(pairs)
        
        ans = []
        for C, D in queries:
            if (C, D) in pairs:
                ans.append(pairs[(C, D)])
                continue
            
            if C not in variables or D not in variables:
                ans.append(-1)
                continue

            if C == D:
                ans.append(1)
                continue
            
            # we know a/b=3, b/b=1
            # do we know a/a? -> no -> because we don't know what b is

            # we know a/b=3, b/c=3
            # do we know a/c? -> yes -> a/c = a/b * b/c = 9
            queue = deque()
            queue.append([C, 1])
            visit = set()
            res = -1.0

            while queue:
                curr, mul = queue.popleft()

                # already checked
                if curr in visit:
                    continue
                visit.add(curr)

                # cannot divide anymore
                if curr not in edges:
                    continue
                
                # divide it
                for div in edges[curr]:
                    if div in visit:
                        continue
                    
                    if div == D:
                        res = mul * pairs[(curr, div)]
                        pairs[(C, D)] = res
                        if res != 0:
                            pairs[(D, C)] = 1/res
                        break
                    
                    queue.append([div, mul * pairs[(curr, div)]])
            
            ans.append(res)
        
        return ans
                    


