class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])
        count = 0
        end = -float('inf')
        for p in intervals:
            if p[0] >= end:
                end = p[1]
                count += 1
            else:
                end = min(end, p[1])
        return len(intervals) - count