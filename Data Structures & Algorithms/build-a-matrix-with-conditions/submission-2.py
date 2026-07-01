class Solution:
    def getPriors(self, k: int, priorities: List[List[int]]) -> List[List[int]]:
        priors = [set() for _ in range(k+1)]

        for prior, later in priorities:
            if later in priors[prior]:
                return []
            priors[later].add(prior)
        
        res = []
        queue = deque()
        
        for i in range(1, k+1):
            if len(priors[i]) == 0:
                queue.append(i)
        
        while queue:
            curr = queue.popleft()
            res.append(curr)

            for i in range(1,k+1):
                if curr in priors[i]:
                    priors[i].remove(curr)
                    if len(priors[i]) == 0:
                        queue.append(i)
        
        return res

    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        rowPriors = self.getPriors(k, rowConditions)
        colPriors = self.getPriors(k, colConditions)

        if len(rowPriors) != k or len(colPriors) != k:
            return []
        
        rowPos = dict()
        colPos = dict()
        for i in range(k):
            rowPos[rowPriors[i]] = i
            colPos[colPriors[i]] = i
        
        res = [[0 for _ in range(k)] for _ in range(k)]
        for i in range(k):
            val = i+1
            res[rowPos[val]][colPos[val]] = val
        
        return res

        
