class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        count = 0
        lastEnd = float('-inf')
        for interval in intervals:
            if interval[0] >= lastEnd:
                # no overlapping
                lastEnd = interval[1]
            else:
                # overlapping, have to remove one
                count += 1
                lastEnd = min(lastEnd, interval[1])

        return count