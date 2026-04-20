class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def calculate_hours(k: int) -> int:
            total = 0
            for pile in piles:
                total += math.ceil(pile / k)
            return total
        
        right = max(piles)
        left = math.ceil(sum(piles) / h)
        # mink = 100

        def binary_search(left: int, right: int, mink: int) -> int:
            if left > right:
                return mink
            
            k = left + (right - left) // 2
            hours = calculate_hours(k)

            if hours <= h:
                # succesfully eat, k is large enough
                if k < mink:
                    mink = k
                return binary_search(left, k-1, mink)
            else:
                # failed to eat, k is not large enough
                return binary_search(k+1, right, mink)
        
        return binary_search(left, right, right)
        