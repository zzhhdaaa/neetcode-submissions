class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        l = 0
        r = len(people) - 1

        count = 0

        while l<=r:
            space = limit - people[r]
            count += 1
            r -= 1

            if space >= people[l]:
                l += 1
        
        return count