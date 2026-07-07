class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        LEN = len(piles)
        TOTAL = sum(piles)
        HALF = TOTAL//2
        memo = dict()
        
        def taketurn(l: int, r: int, isAlice: bool) -> int: # return alice score
            if l>r:
                return 0
            
            key = (l, r, isAlice)
            if key in memo:
                return memo[key]
            
            # alice wants to maximize score
            if isAlice:
                takel = piles[l] + taketurn(l+1, r, False)
                taker = piles[r] + taketurn(l, r-1, False)
                memo[key] = max(takel, taker)
                return memo[key]
            # bob wants to minimize score
            else:
                takel = taketurn(l+1, r, True)
                taker = taketurn(l, r-1, True)
                memo[key] = max(takel, taker)
                return memo[key]
        
        return taketurn(0, LEN-1, True) > HALF
            
