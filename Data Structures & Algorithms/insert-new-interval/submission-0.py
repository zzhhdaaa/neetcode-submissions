import bisect
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # first find a pos to insert
        # then do a one-pass merge

        n = bisect.bisect_left(intervals, newInterval)
        intervals.insert(n, newInterval)
        
        res = []
        prevend = float('-inf')
        for start, end in intervals:
            if start > prevend:
                res.append([start, end])
                prevend = end
            else:
                # merge
                res[-1][1] = max(res[-1][1], end)
                prevend = res[-1][1]
        
        return res