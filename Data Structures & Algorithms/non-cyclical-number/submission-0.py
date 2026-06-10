class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()
        curr = n
        while True:
            if curr in visit:
                return False
            visit.add(curr)

            text = str(curr)
            total = 0
            for c in text:
                total += int(c)**2
            if total == 1:
                return True
            curr = total