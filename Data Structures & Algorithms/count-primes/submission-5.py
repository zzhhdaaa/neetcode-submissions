class Solution:
    def countPrimes(self, n: int) -> int:
        # sieve: mark composite numbers
        sieve = [False for _ in range(n)]
        res = 0
        for num in range(2, n):
            if not sieve[num]: # this means prime
                res += 1
                for i in range(num*num, n, num):
                    sieve[i] = True
        return res


