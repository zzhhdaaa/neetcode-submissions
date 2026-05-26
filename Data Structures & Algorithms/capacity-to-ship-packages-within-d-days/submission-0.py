class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # largest possible: sum(weights)
        # smallest possible: 1
        l = 1
        r = sum(weights)

        def can_load(cap: int):
            curr = cap
            res = 1
            for weight in weights:
                if weight > cap:
                    return False

                if weight <= curr:
                    curr -= weight
                else:
                    curr = cap - weight
                    res += 1
            return res <= days

        while l<r:
            m = (l+r)//2

            if can_load(m):
                r = m
            else:
                l = m + 1
        
        return l