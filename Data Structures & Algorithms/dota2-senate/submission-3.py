class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # what is optimum?
        # when taking right, each player will try to ban the earliest opponent -> queue

        rq = deque()
        dq = deque()
        n = len(senate)

        for i in range(n):
            if senate[i] == "R":
                rq.append(i)
            else:
                dq.append(i)
        
        while rq and dq:
            r = rq.popleft()
            d = dq.popleft()

            if r < d:
                rq.append(r+n)
            else:
                dq.append(d+n)
        
        return "Radiant" if rq else "Dire"
        
