class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_to_idx = defaultdict(list) # email to account idx
        emails = set()
        edges = []

        for i in range(len(accounts)):
            prev = None
            for j in range(1, len(accounts[i])):
                email = accounts[i][j]
                email_to_idx[email].append(i)
                if prev is not None:
                    edges.append([prev, email])
                prev = email
                emails.add(email)
        
        visit = set()
        res = []
        for email in emails:
            if email in visit:
                continue
            
            name = accounts[email_to_idx[email][0]][0]
            queue = deque()
            queue.append(email)
            visit.add(email)

            merge = [name]
        
            while queue:
                email = queue.popleft()
                merge.append(email)

                for edge in edges:
                    if edge[0] == email and edge[1] not in visit:
                        finished = False
                        queue.append(edge[1])
                        visit.add(edge[1])
                    elif edge[1] == email and edge[0] not in visit:
                        finished = False
                        queue.append(edge[0])
                        visit.add(edge[0])
                
            res.append(merge.copy())
        
        return res
        

