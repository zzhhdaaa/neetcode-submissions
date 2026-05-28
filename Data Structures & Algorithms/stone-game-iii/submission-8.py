sys.setrecursionlimit(100000)

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        # 1, 2, -3, 4, 5, 6, 100
        # _
        # ____
        # ________

        # can greedy gaurantee the highest outcome? - No
        SUM = sum(stoneValue)
        LEN = len(stoneValue)
        memo = dict()

        def take_turns(i: int, is_alice: bool):
            # we return how many point alice can get from (i, is_alice) onward
            if i >= LEN:
                return 0
            
            if (i, is_alice) in memo:
                return memo[(i, is_alice)]
            
            # take 1, 2, 3
            taken = 0
            res = float('-inf') if is_alice else float('inf')
            for take in range(3):
                if i+take >= LEN:
                    continue
                taken += stoneValue[i+take]
                if is_alice:
                    # alice wants to maximize the outcome
                    res = max(res, take_turns(i+take+1, False) + taken)
                else:
                    # bob wants to minimize the outcome
                    res = min(res, take_turns(i+take+1, True))
            
            memo[(i, is_alice)] = res
            return res
        
        alice_max = take_turns(0, True)
        if alice_max > SUM / 2:
            return "Alice"
        elif alice_max < SUM / 2:
            return "Bob"
        else:
            return "Tie"