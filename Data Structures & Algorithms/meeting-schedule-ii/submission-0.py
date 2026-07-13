"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0
        maxRooms = 0
        for interval in intervals:
            start = interval.start
            count = 0
            for other in intervals:
                if other.start <= start and start < other.end:
                    count += 1

            maxRooms = max(count, maxRooms)

        return maxRooms