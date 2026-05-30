"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda interval: interval.start)

        bookings = []
        res = 0

        for interval in intervals:
            start, end = interval.start, interval.end

            while len(bookings) != 0 and start >= bookings[0]:
                heapq.heappop(bookings)
                
            heapq.heappush(bookings, end)
            res = max(res, len(bookings))
        
        return res
            
