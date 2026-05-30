"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        bookings = [] # each item is [time, action], action: -1 means end, +1 means start

        for interval in intervals:
            bookings.append([interval.start, +1])
            bookings.append([interval.end, -1])
        
        bookings.sort(key=lambda x: (x[0], x[1]))

        curr = 0
        res = 0
        for booking in bookings:
            curr += booking[1]
            res = max(res, curr)
        
        return res
            
