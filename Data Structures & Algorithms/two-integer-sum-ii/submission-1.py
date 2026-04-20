class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lpt = 0
        rpt = len(numbers)-1
        summary = numbers[lpt] + numbers[rpt]

        while summary != target:
            if summary < target:
                lpt += 1
            elif summary > target:
                rpt -= 1
            summary = numbers[lpt] + numbers[rpt]
        
        return [lpt+1, rpt+1]
        
        