class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        currStart = intervals[0][0]
        currEnd = intervals[0][1]

        for start, end in intervals:
            if start > currEnd:
                res.append([currStart, currEnd])
                currStart = start
                currEnd = end
            elif end < currEnd:
                continue
            else:
                currEnd = end
        res.append([currStart, currEnd])

        return res
