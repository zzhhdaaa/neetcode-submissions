class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # what is optimum?
        # when taking right, each player will try to ban the earliest opponent -> queue / ptr
        rbanned = 0
        dbanned = 0
        banned = set()

        while True:
            ronly = True
            donly = True
            for i in range(len(senate)):
                if i in banned:
                    continue
                
                if senate[i] == "R":
                    if rbanned > 0:
                        rbanned -= 1
                        banned.add(i)
                    else:
                        donly = False
                        dbanned += 1
                else:
                    if dbanned > 0:
                        dbanned -= 1
                        banned.add(i)
                    else:
                        ronly = False
                        rbanned += 1
            
            if ronly:
                return "Radiant"
            if donly:
                return "Dire"
