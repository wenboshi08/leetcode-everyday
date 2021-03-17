class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        start = intervals[0][0]
        end = intervals[0][1]
        count = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] == start:
                count += 1
                end = max(end, intervals[i][1])
            else:
                if intervals[i][1] > end:
                    start = intervals[i][0]
                    end = intervals[i][1]
                else:
                    count += 1
        return len(intervals) - count