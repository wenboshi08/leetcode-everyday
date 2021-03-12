class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        res = []
        start = intervals[0][0]
        end = intervals[0][1]
        for p in intervals:
            if p[0] <= end:
                end = max(p[1], end)
            else:
                res.append([start, end])
                start = p[0]
                end = p[1]
        res.append([start, end])
        return res