class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustCount = dict()
        trustedCount = dict()

        for t, ted in trust:
            trustCount[t] = trustCount.get(t, 0) + 1
            trustedCount[ted] = trustedCount.get(ted, 0) + 1
        
        res = -1
        foundJudge = False
        for i in range(1, n+1):
            if i not in trustCount and trustedCount.get(i, 0) == n - 1:
                if foundJudge:
                    return -1
                else:
                    res = i
                    foundJudge = True
        
        return res