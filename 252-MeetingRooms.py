class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x: x[0])
        end = 0
        for p in intervals:
            if p[0] >= end:
                end = p[1]
            else:
                return False
        return True
