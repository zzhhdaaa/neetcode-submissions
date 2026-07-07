class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        changes = dict()
        changes[5] = 0
        changes[10] = 0
        changes[20] = 0

        for bill in bills:
            change = bill - 5

            if change == 15:
                if changes[10] > 0 and changes[5] > 0:
                    changes[10] -= 1
                    changes[5] -= 1
                    changes[20] += 1
                elif changes[5] >= 3:
                    changes[5] -= 3
                    changes[20] += 1
                else:
                    return False
            elif change == 5:
                if changes[5] > 0:
                    changes[5] -= 1
                    changes[10] += 1
                else:
                    return False
            elif change == 0:
                changes[5] += 1
        
        return True
