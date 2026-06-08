class Solution:
    def countPrimes(self, n: int) -> int:
        # smallest prime factor
        spf = [i for i in range(n)]
        for i in range(2, int(n**0.5)+1):
            if spf[i] != i:
                continue
            for j in range(i*i, n, i):
                # check if not yet marked with a smaller prime
                if spf[j] == j:
                    spf[j] = i
        
        res = 0
        for i in range(2, n):
            if spf[i] == i:
                res += 1
        
        return res


