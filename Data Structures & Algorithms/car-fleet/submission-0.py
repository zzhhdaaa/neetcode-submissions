class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # [4, 1, 0, 7]
        # [2, 2, 1, 1]
        # 0 1 2 3 4 5 6 7 8 9
        # . .     .     .
        
        positions, speeds = zip(*sorted(zip(position, speed)))
        prevEta = 0
        fleets = 0

        for i in range(len(positions)-1, -1, -1):
            eta = (target - positions[i]) / speeds[i]
            if eta > prevEta:
                prevEta = eta
                fleets += 1
        
        return fleets